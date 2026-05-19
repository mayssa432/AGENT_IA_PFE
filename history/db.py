# -*- coding: utf-8 -*-
"""
history/db.py
=============
Historique centralisé — base SQLite légère.

Tables :
  events  — chaque action de l'agent (analyse, correction, génération, sync mock)
  metrics — compteurs/métriques agrégées par jour

Usage :
    from history.db import log_event, get_history, get_stats

    log_event("selector_fix", {"po_file": "AuthPO.java", "broken": 5, "fixed": 3})
    rows = get_history(event_type="selector_fix", limit=20)
    stats = get_stats()
"""

import json
import sqlite3
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ── Chemin de la base ─────────────────────────────────────────────────────
_ROOT      = Path(__file__).parent.parent
DB_PATH    = _ROOT / "output" / "agent_history.db"

# Types d'événements
EVENT_ANALYSIS    = "analysis"
EVENT_SELECTOR    = "selector_fix"
EVENT_SCENARIO    = "scenario_gen"
EVENT_MOCK_SYNC   = "mock_sync"
EVENT_PIPELINE    = "pipeline"


# ═══════════════════════════════════════════════════════════════════════════
#  INITIALISATION
# ═══════════════════════════════════════════════════════════════════════════

def get_db(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Ouvre (et initialise si nécessaire) la base SQLite."""
    path = db_path or DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row          # accès par nom de colonne
    conn.execute("PRAGMA journal_mode=WAL")  # écriture concurrente
    conn.execute("PRAGMA foreign_keys=ON")
    _create_tables(conn)
    return conn


def _create_tables(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS events (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type  TEXT    NOT NULL,
            status      TEXT    NOT NULL DEFAULT 'ok',
            ts          TEXT    NOT NULL,
            duration_ms INTEGER,
            payload     TEXT,           -- JSON
            summary     TEXT            -- courte description lisible
        );

        CREATE INDEX IF NOT EXISTS idx_events_type ON events(event_type);
        CREATE INDEX IF NOT EXISTS idx_events_ts   ON events(ts);

        CREATE TABLE IF NOT EXISTS daily_stats (
            day         TEXT NOT NULL,
            event_type  TEXT NOT NULL,
            count       INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (day, event_type)
        );
    """)
    conn.commit()


# ═══════════════════════════════════════════════════════════════════════════
#  ÉCRITURE
# ═══════════════════════════════════════════════════════════════════════════

def log_event(
    event_type: str,
    payload:    Dict[str, Any],
    status:     str = "ok",
    summary:    Optional[str] = None,
    duration_ms: Optional[int] = None,
    db_path:    Optional[Path] = None,
) -> int:
    """
    Enregistre un événement dans la base.

    Paramètres
    ----------
    event_type  : une des constantes EVENT_* (ou chaîne libre)
    payload     : dict sérialisable en JSON
    status      : 'ok' | 'error' | 'partial'
    summary     : texte court affiché dans l'UI
    duration_ms : durée de l'opération en millisecondes
    db_path     : chemin alternatif pour les tests

    Retourne
    --------
    id de la ligne insérée
    """
    ts = datetime.now(timezone.utc).isoformat()
    day = ts[:10]  # YYYY-MM-DD

    if summary is None:
        summary = _auto_summary(event_type, payload)

    payload_json = json.dumps(payload, ensure_ascii=False, default=str)

    conn = get_db(db_path)
    try:
        cur = conn.execute(
            """INSERT INTO events (event_type, status, ts, duration_ms, payload, summary)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (event_type, status, ts, duration_ms, payload_json, summary),
        )
        row_id = cur.lastrowid

        # Mise à jour des compteurs journaliers
        conn.execute(
            """INSERT INTO daily_stats (day, event_type, count) VALUES (?, ?, 1)
               ON CONFLICT(day, event_type) DO UPDATE SET count = count + 1""",
            (day, event_type),
        )
        conn.commit()
        return row_id
    finally:
        conn.close()


def _auto_summary(event_type: str, payload: Dict[str, Any]) -> str:
    """Génère un résumé lisible automatiquement."""
    if event_type == EVENT_ANALYSIS:
        return (
            f"Analyse : {payload.get('files', '?')} fichiers, "
            f"{payload.get('issues', '?')} problèmes"
        )
    if event_type == EVENT_SELECTOR:
        return (
            f"Correction XPath : {payload.get('broken', '?')} cassés → "
            f"{payload.get('fixed', '?')} corrigés ({payload.get('po_file', '?')})"
        )
    if event_type == EVENT_SCENARIO:
        return (
            f"Scénarios BDD : {payload.get('scenario_count', '?')} scénarios, "
            f"{payload.get('step_count', '?')} steps ({payload.get('po_file', '?')})"
        )
    if event_type == EVENT_MOCK_SYNC:
        return (
            f"Sync mock : {payload.get('diffs_found', '?')} différences "
            f"({payload.get('mock_id', '?')})"
        )
    if event_type == EVENT_PIPELINE:
        return f"Pipeline E2E : {payload.get('pages_path', '?')}"
    return f"{event_type} : {str(payload)[:80]}"


# ═══════════════════════════════════════════════════════════════════════════
#  LECTURE
# ═══════════════════════════════════════════════════════════════════════════

def get_history(
    event_type: Optional[str] = None,
    status:     Optional[str] = None,
    limit:      int = 50,
    offset:     int = 0,
    db_path:    Optional[Path] = None,
) -> List[Dict[str, Any]]:
    """
    Retourne les derniers événements.

    Retourne une liste de dicts avec les champs :
      id, event_type, status, ts, duration_ms, payload (dict), summary
    """
    conn = get_db(db_path)
    try:
        where_clauses = []
        params: List[Any] = []

        if event_type:
            where_clauses.append("event_type = ?")
            params.append(event_type)
        if status:
            where_clauses.append("status = ?")
            params.append(status)

        where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""

        rows = conn.execute(
            f"""SELECT id, event_type, status, ts, duration_ms, payload, summary
                FROM events
                {where_sql}
                ORDER BY id DESC
                LIMIT ? OFFSET ?""",
            params + [limit, offset],
        ).fetchall()

        result = []
        for row in rows:
            d = dict(row)
            try:
                d["payload"] = json.loads(d["payload"]) if d["payload"] else {}
            except Exception:
                d["payload"] = {}
            result.append(d)
        return result

    finally:
        conn.close()


def get_stats(db_path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Retourne les statistiques globales et par type d'événement.
    """
    conn = get_db(db_path)
    try:
        total = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        by_type = {
            row["event_type"]: row["count"]
            for row in conn.execute(
                "SELECT event_type, COUNT(*) as count FROM events GROUP BY event_type"
            ).fetchall()
        }
        by_status = {
            row["status"]: row["count"]
            for row in conn.execute(
                "SELECT status, COUNT(*) as count FROM events GROUP BY status"
            ).fetchall()
        }
        # Activité des 7 derniers jours
        daily = [
            {"day": row["day"], "event_type": row["event_type"], "count": row["count"]}
            for row in conn.execute(
                """SELECT day, event_type, count
                   FROM daily_stats
                   ORDER BY day DESC
                   LIMIT 70"""
            ).fetchall()
        ]
        # Dernière activité par type
        last_by_type = {}
        for row in conn.execute(
            "SELECT event_type, MAX(ts) as last_ts FROM events GROUP BY event_type"
        ).fetchall():
            last_by_type[row["event_type"]] = row["last_ts"]

        return {
            "total_events":   total,
            "by_type":        by_type,
            "by_status":      by_status,
            "daily_activity": daily,
            "last_by_type":   last_by_type,
        }
    finally:
        conn.close()


def clear_history(event_type: Optional[str] = None, db_path: Optional[Path] = None) -> int:
    """
    Supprime les événements (tous ou d'un type donné).
    Retourne le nombre de lignes supprimées.
    """
    conn = get_db(db_path)
    try:
        if event_type:
            cur = conn.execute("DELETE FROM events WHERE event_type = ?", (event_type,))
        else:
            cur = conn.execute("DELETE FROM events")
        conn.execute("DELETE FROM daily_stats" + (" WHERE event_type = ?" if event_type else ""),
                     ([event_type] if event_type else []))
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()
