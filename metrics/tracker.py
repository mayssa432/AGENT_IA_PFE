"""
metrics/tracker.py — Livrable #8 : Métriques de performance en temps réel
=========================================================================
Enregistre chaque opération agent (durée, statut, résultat) dans SQLite.

Tables
------
runs : id, ts, operation, duration_ms, status, details_json

API publique
------------
track(operation, duration_ms, status, **details)
get_runs(operation=None, limit=50)   → list[dict]
get_kpis()                           → dict (agrégats globaux + par opération)
clear_metrics(operation=None)        → int (nb lignes supprimées)
"""

from __future__ import annotations

import json
import sqlite3
import time
import threading
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Optional

# ── Constantes ────────────────────────────────────────────────────────────
OP_ANALYSIS   = "analysis"
OP_SELECTOR   = "selector_fix"
OP_SCENARIO   = "scenario_gen"
OP_MOCK_SYNC  = "mock_sync"
OP_PIPELINE   = "pipeline"

STATUS_SUCCESS = "success"
STATUS_ERROR   = "error"

_DB_PATH = Path(__file__).parent.parent / "metrics.db"
_lock = threading.Lock()

# ── Initialisation ────────────────────────────────────────────────────────

def _get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(str(_DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def _ensure_schema() -> None:
    with _lock, _get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS runs (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                ts           TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
                operation    TEXT    NOT NULL,
                duration_ms  INTEGER NOT NULL,
                status       TEXT    NOT NULL DEFAULT 'success',
                details_json TEXT
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_runs_op_ts ON runs(operation, ts)")
        conn.commit()


# Initialisation au chargement du module
try:
    _ensure_schema()
except Exception:
    pass  # CI / environnements sans écriture disque

# ── API publique ──────────────────────────────────────────────────────────

def track(
    operation: str,
    duration_ms: int,
    status: str = STATUS_SUCCESS,
    **details: Any,
) -> None:
    """Insère un enregistrement de run."""
    details_str = json.dumps(details, ensure_ascii=False) if details else None
    try:
        with _lock, _get_conn() as conn:
            conn.execute(
                "INSERT INTO runs (operation, duration_ms, status, details_json) VALUES (?,?,?,?)",
                (operation, int(duration_ms), status, details_str),
            )
            conn.commit()
    except Exception:
        pass  # Ne jamais bloquer l'opération principale


def get_runs(operation: Optional[str] = None, limit: int = 50) -> list[dict]:
    """Retourne les runs récents (les plus récents en premier)."""
    try:
        with _get_conn() as conn:
            if operation:
                rows = conn.execute(
                    "SELECT * FROM runs WHERE operation=? ORDER BY ts DESC, id DESC LIMIT ?",
                    (operation, limit),
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM runs ORDER BY ts DESC, id DESC LIMIT ?",
                    (limit,),
                ).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            if d.get("details_json"):
                try:
                    d["details"] = json.loads(d["details_json"])
                except Exception:
                    d["details"] = {}
            del d["details_json"]
            result.append(d)
        return result
    except Exception:
        return []


def get_kpis() -> dict:
    """
    Retourne des agrégats globaux et par opération.

    Retourne
    --------
    {
      total_runs, success_rate_pct, avg_duration_ms, last_run_ts,
      by_operation: {op: {count, success_rate_pct, avg_duration_ms, last_ts}}
    }
    """
    try:
        with _get_conn() as conn:
            row = conn.execute("""
                SELECT
                    COUNT(*)                                      AS total,
                    ROUND(100.0*SUM(status='success')/COUNT(*),1) AS sr,
                    ROUND(AVG(duration_ms))                       AS avg_ms,
                    MAX(ts)                                       AS last_ts
                FROM runs
            """).fetchone()
            total    = row["total"] or 0
            sr       = row["sr"]   or 0.0
            avg_ms   = int(row["avg_ms"] or 0)
            last_ts  = row["last_ts"] or ""

            by_op_rows = conn.execute("""
                SELECT
                    operation,
                    COUNT(*)                                      AS cnt,
                    ROUND(100.0*SUM(status='success')/COUNT(*),1) AS sr,
                    ROUND(AVG(duration_ms))                       AS avg_ms,
                    MAX(ts)                                       AS last_ts
                FROM runs
                GROUP BY operation
                ORDER BY cnt DESC
            """).fetchall()

        by_op = {}
        for r in by_op_rows:
            by_op[r["operation"]] = {
                "count":            r["cnt"],
                "success_rate_pct": r["sr"],
                "avg_duration_ms":  int(r["avg_ms"] or 0),
                "last_ts":          r["last_ts"],
            }

        return {
            "total_runs":        total,
            "success_rate_pct":  sr,
            "avg_duration_ms":   avg_ms,
            "last_run_ts":       last_ts,
            "by_operation":      by_op,
        }
    except Exception:
        return {
            "total_runs": 0,
            "success_rate_pct": 0.0,
            "avg_duration_ms": 0,
            "last_run_ts": "",
            "by_operation": {},
        }


def clear_metrics(operation: Optional[str] = None) -> int:
    """Supprime tous les runs (ou ceux d'une opération donnée)."""
    try:
        with _lock, _get_conn() as conn:
            if operation:
                cur = conn.execute("DELETE FROM runs WHERE operation=?", (operation,))
            else:
                cur = conn.execute("DELETE FROM runs")
            conn.commit()
            return cur.rowcount
    except Exception:
        return 0


# ── Décorateur utilitaire ─────────────────────────────────────────────────

def timed_operation(operation: str) -> Callable:
    """
    Décorateur : mesure le temps d'exécution de la fonction décorée
    et insère automatiquement un enregistrement dans metrics.

    Usage
    -----
    @timed_operation(OP_SELECTOR)
    def my_fix_function(po_file):
        ...
        return {"fixed": 3}

    La valeur de retour est transmise inchangée.
    Si la fonction lève une exception, status='error' est enregistré.
    """
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args, **kwargs):
            t0 = time.perf_counter()
            status = STATUS_SUCCESS
            details: dict = {}
            try:
                result = fn(*args, **kwargs)
                if isinstance(result, dict):
                    details = {k: v for k, v in result.items() if isinstance(v, (int, float, str, bool))}
                return result
            except Exception as exc:
                status = STATUS_ERROR
                details = {"error": str(exc)[:200]}
                raise
            finally:
                duration_ms = int((time.perf_counter() - t0) * 1000)
                track(operation, duration_ms, status, **details)
        return wrapper
    return decorator
