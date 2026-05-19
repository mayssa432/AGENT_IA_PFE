# -*- coding: utf-8 -*-
"""
mcp_agent_pfe.py
================
Serveur MCP (Model Context Protocol) pour l'agent IA PFE — Projet App TV.

Expose les outils de l'agent directement dans VS Code Copilot / Claude / tout client MCP.

Outils disponibles :
  • analyze_page_objects   — Analyse les Page Objects Java du projet TV
  • fix_selectors          — Corrige les sélecteurs XPath/ID cassés d'un fichier
  • generate_scenarios     — Génère les scénarios Gherkin BDD via Groq LLM
  • run_pipeline           — Lance le pipeline complet E2E (analyse + correction + rapport)
  • get_history            — Retourne l'historique SQLite des opérations
  • get_metrics            — Retourne les KPIs de performance
  • list_page_objects      — Liste les fichiers Java Page Objects disponibles
  • get_dom_report         — Retourne un rapport DOM pour un fichier Page Object

Usage (stdio — pour VS Code / Claude Desktop) :
    python mcp_agent_pfe.py

Usage (dev avec inspector) :
    mcp dev mcp_agent_pfe.py
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

# ─── Chemins du projet ─────────────────────────────────────────────────────
ROOT_DIR  = Path(__file__).parent
PAGES_DIR = ROOT_DIR / "AGENT_IA_PFE" / "src" / "test" / "java" / \
            "com" / "orange" / "otvp" / "automation" / "pages" / "mobile"
REPORTS_DIR = ROOT_DIR / "dom_reports"
OUTPUT_DIR  = ROOT_DIR / "output"

# Charger .env
try:
    from dotenv import load_dotenv
    load_dotenv(ROOT_DIR / ".env")
except ImportError:
    pass

# ─── Imports internes (avec fallback) ──────────────────────────────────────
sys.path.insert(0, str(ROOT_DIR))

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    raise SystemExit(
        "❌ Package 'mcp' non installé.\n"
        "   Installez-le avec : pip install 'mcp[cli]'"
    )

try:
    from history.db import get_history, get_stats, log_event, EVENT_SELECTOR, EVENT_SCENARIO, EVENT_ANALYSIS
    _HAS_HISTORY = True
except ImportError:
    _HAS_HISTORY = False

try:
    from metrics.tracker import get_kpis, get_runs
    _HAS_METRICS = True
except ImportError:
    _HAS_METRICS = False

try:
    from analyzers.xpath_analyzer import XPathAnalyzer
    from analyzers.file_parser import PageObjectParser
    from analyzers.annotation_checker import AnnotationChecker
    from analyzers.duplicate_detector import DuplicateDetector
    _HAS_ANALYZERS = True
except ImportError:
    _HAS_ANALYZERS = False

# ─── Initialisation FastMCP ─────────────────────────────────────────────────
mcp = FastMCP(
    name="mcp_agent_pfe",
    instructions=(
        "Agent IA pour la maintenance automatique des tests mobiles du projet App TV Orange. "
        "Analyse les Page Objects Java Appium, corrige les sélecteurs XPath cassés, "
        "génère des scénarios Gherkin BDD via LLM, et pilote le pipeline E2E complet."
    ),
)


# ═══════════════════════════════════════════════════════════════════════════
#  OUTIL 1 — Lister les Page Objects Java
# ═══════════════════════════════════════════════════════════════════════════

@mcp.tool()
def list_page_objects() -> str:
    """
    Liste tous les fichiers Java Page Objects disponibles dans le projet TV.
    Retourne le nom de chaque fichier avec son nombre de lignes.
    """
    if not PAGES_DIR.exists():
        return json.dumps({"error": f"Dossier pages introuvable : {PAGES_DIR}", "files": []})

    java_files = sorted(PAGES_DIR.glob("*.java"))
    result = []
    for f in java_files:
        lines = len(f.read_text(encoding="utf-8", errors="replace").splitlines())
        result.append({"file": f.name, "lines": lines, "path": str(f)})

    return json.dumps({
        "total": len(result),
        "pages_dir": str(PAGES_DIR),
        "files": result
    }, ensure_ascii=False, indent=2)


# ═══════════════════════════════════════════════════════════════════════════
#  OUTIL 2 — Analyser les Page Objects
# ═══════════════════════════════════════════════════════════════════════════

@mcp.tool()
def analyze_page_objects(file_name: str = "") -> str:
    """
    Analyse les Page Objects Java du projet App TV pour détecter :
    - Sélecteurs XPath/ID invalides ou suspects
    - Doublons de sélecteurs
    - Annotations manquantes ou mal formées

    Args:
        file_name: Nom du fichier Java à analyser (ex: "LoginPO.java").
                   Si vide, analyse tous les fichiers du projet.

    Returns:
        Rapport JSON avec les problèmes détectés par fichier.
    """
    if not _HAS_ANALYZERS:
        return json.dumps({"error": "Module analyzers non disponible"})

    if not PAGES_DIR.exists():
        return json.dumps({"error": f"Dossier pages introuvable : {PAGES_DIR}"})

    if file_name:
        target = PAGES_DIR / file_name
        java_files = [target] if target.exists() else []
        if not java_files:
            return json.dumps({"error": f"Fichier introuvable : {file_name}"})
    else:
        java_files = sorted(PAGES_DIR.glob("*.java"))

    xpath_analyzer    = XPathAnalyzer()
    annotation_checker = AnnotationChecker()
    dup_detector      = DuplicateDetector()

    results = []
    total_issues = 0

    for java_file in java_files:
        path_str = str(java_file)
        issues = []
        issues.extend(xpath_analyzer.validate(path_str))
        issues.extend(annotation_checker.check(path_str))
        issues.extend(dup_detector.detect(path_str))
        total_issues += len(issues)

        results.append({
            "file": java_file.name,
            "issues_count": len(issues),
            "issues": issues[:20],  # max 20 par fichier pour la lisibilité
        })

    if _HAS_HISTORY:
        log_event(EVENT_ANALYSIS, {"files": len(java_files), "issues": total_issues})

    return json.dumps({
        "analyzed": len(java_files),
        "total_issues": total_issues,
        "status": "ok" if total_issues == 0 else "issues_found",
        "results": results,
    }, ensure_ascii=False, indent=2, default=str)


# ═══════════════════════════════════════════════════════════════════════════
#  OUTIL 3 — Corriger les sélecteurs d'un fichier
# ═══════════════════════════════════════════════════════════════════════════

@mcp.tool()
def fix_selectors(file_name: str, dry_run: bool = True) -> str:
    """
    Corrige automatiquement les sélecteurs XPath/ID cassés dans un Page Object Java.
    Utilise le dernier snapshot DOM disponible pour valider et suggérer des corrections.

    Args:
        file_name: Nom du fichier Java à corriger (ex: "FipLivePO.java").
        dry_run: Si True (défaut), affiche les corrections sans les écrire.
                 Si False, modifie le fichier Java directement.

    Returns:
        JSON avec les corrections appliquées (ou à appliquer en dry_run).
    """
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONPATH"] = str(ROOT_DIR)

    args = [sys.executable, str(ROOT_DIR / "demo_selector_fix.py")]
    if file_name:
        args += ["--po-file", file_name]
    if dry_run:
        args += ["--dry-run"]

    try:
        result = subprocess.run(
            args, capture_output=True, text=True,
            timeout=60, cwd=str(ROOT_DIR), env=env,
            encoding="utf-8", errors="replace"
        )
        output = result.stdout + (("\n[STDERR]\n" + result.stderr) if result.stderr.strip() else "")
        success = result.returncode == 0

        if _HAS_HISTORY and success:
            log_event(EVENT_SELECTOR, {"po_file": file_name, "dry_run": dry_run})

        return json.dumps({
            "success": success,
            "file": file_name,
            "dry_run": dry_run,
            "output": output[-2000:],
        }, ensure_ascii=False, indent=2)
    except subprocess.TimeoutExpired:
        return json.dumps({"success": False, "error": "Timeout (60s)"})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})


# ═══════════════════════════════════════════════════════════════════════════
#  OUTIL 4 — Générer des scénarios Gherkin BDD
# ═══════════════════════════════════════════════════════════════════════════

@mcp.tool()
def generate_scenarios(file_name: str = "", batch: int = 1, offline: bool = False) -> str:
    """
    Génère des scénarios Gherkin BDD et des Step Definitions Java pour un Page Object.
    Utilise Groq LLM (llama-3.3-70b-versatile) si la clé API est configurée.

    Args:
        file_name: Nom du fichier Java source (ex: "AuthenticationPO.java").
                   Si vide, utilise le premier fichier du batch.
        batch:     Nombre de Page Objects à traiter en séquence (défaut: 1, max: 5).
        offline:   Si True, utilise des templates statiques sans appel LLM.

    Returns:
        JSON avec les fichiers générés (.feature, StepDefinitions, Runner).
    """
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONPATH"] = str(ROOT_DIR)

    args = [sys.executable, str(ROOT_DIR / "demo_scenario_generator.py"),
            "--batch", str(min(batch, 5))]
    if file_name:
        args += ["--po-file", file_name]
    if offline:
        args += ["--offline"]

    try:
        result = subprocess.run(
            args, capture_output=True, text=True,
            timeout=120, cwd=str(ROOT_DIR), env=env,
            encoding="utf-8", errors="replace"
        )
        output = result.stdout
        success = result.returncode == 0

        # Extraire le résumé de la sortie
        summary_lines = [l for l in output.splitlines()
                         if any(k in l for k in ("Source LLM", "Scénarios", "Step Def", "SUCCÈS", "BILAN", "✅", "❌"))]

        if _HAS_HISTORY and success:
            log_event(EVENT_SCENARIO, {"file": file_name, "batch": batch})

        return json.dumps({
            "success": success,
            "file": file_name or f"batch({batch})",
            "offline": offline,
            "summary": "\n".join(summary_lines[-20:]),
            "output_dir": str(ROOT_DIR / "output" / "scenario_generator"),
        }, ensure_ascii=False, indent=2)
    except subprocess.TimeoutExpired:
        return json.dumps({"success": False, "error": "Timeout (120s) — essayez --offline"})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})


# ═══════════════════════════════════════════════════════════════════════════
#  OUTIL 5 — Pipeline E2E complet
# ═══════════════════════════════════════════════════════════════════════════

@mcp.tool()
def run_pipeline(dry_run: bool = True) -> str:
    """
    Lance le pipeline complet de l'agent IA PFE en mode simulation :
      1. Analyse de tous les Page Objects Java
      2. Détection des sélecteurs cassés
      3. Corrections automatiques
      4. Génération du rapport JSON

    Args:
        dry_run: Si True (défaut), simule sans modifier les fichiers ni se connecter à Appium.

    Returns:
        JSON avec le résumé du pipeline (28 fichiers analysés, corrections, durée).
    """
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONPATH"] = str(ROOT_DIR)

    args = [sys.executable, str(ROOT_DIR / "orchestrate.py"),
            "--pages", str(PAGES_DIR)]
    if dry_run:
        args += ["--dry-run"]

    try:
        result = subprocess.run(
            args, capture_output=True, text=True,
            timeout=90, cwd=str(ROOT_DIR), env=env,
            encoding="utf-8", errors="replace"
        )
        output = result.stdout
        success = result.returncode == 0

        summary_lines = [l for l in output.splitlines()
                         if any(k in l for k in ("fichier", "correction", "✅", "❌", "ÉTAPE", "rapport", "RÉSUMÉ"))]

        return json.dumps({
            "success": success,
            "dry_run": dry_run,
            "summary": "\n".join(summary_lines[-30:]),
            "returncode": result.returncode,
        }, ensure_ascii=False, indent=2)
    except subprocess.TimeoutExpired:
        return json.dumps({"success": False, "error": "Timeout (90s)"})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})


# ═══════════════════════════════════════════════════════════════════════════
#  OUTIL 6 — Historique SQLite
# ═══════════════════════════════════════════════════════════════════════════

@mcp.tool()
def get_history(limit: int = 20, event_type: str = "") -> str:
    """
    Retourne l'historique des opérations de l'agent (corrections, analyses, génération).
    Les données sont stockées dans history.db (SQLite).

    Args:
        limit:      Nombre maximum d'événements à retourner (défaut: 20).
        event_type: Filtrer par type : "analysis", "selector", "scenario", "mock_sync".
                    Si vide, retourne tous les types.

    Returns:
        JSON avec la liste des événements et les statistiques globales.
    """
    if not _HAS_HISTORY:
        return json.dumps({"error": "Module history non disponible"})

    from history.db import get_history as _get_history, get_stats
    rows = _get_history(limit=limit, event_type=event_type if event_type else None)
    stats = get_stats()

    return json.dumps({
        "events": rows,
        "stats": stats,
        "total_shown": len(rows),
    }, ensure_ascii=False, indent=2, default=str)


# ═══════════════════════════════════════════════════════════════════════════
#  OUTIL 7 — Métriques de performance
# ═══════════════════════════════════════════════════════════════════════════

@mcp.tool()
def get_metrics(limit: int = 10) -> str:
    """
    Retourne les KPIs de performance de l'agent (durées moyennes, compteurs).
    Les données sont stockées dans metrics.db (SQLite).

    Args:
        limit: Nombre de dernières exécutions à inclure dans l'historique (défaut: 10).

    Returns:
        JSON avec les KPIs agrégés par type d'opération et les dernières exécutions.
    """
    if not _HAS_METRICS:
        return json.dumps({"error": "Module metrics non disponible"})

    kpis = get_kpis()
    runs = get_runs(limit=limit)

    return json.dumps({
        "kpis": kpis,
        "recent_runs": runs,
        "generated_at": datetime.now().isoformat(),
    }, ensure_ascii=False, indent=2, default=str)


# ═══════════════════════════════════════════════════════════════════════════
#  OUTIL 8 — Rapport DOM d'un Page Object
# ═══════════════════════════════════════════════════════════════════════════

@mcp.tool()
def get_dom_report(file_name: str) -> str:
    """
    Retourne le rapport de validation DOM pré-calculé pour un Page Object Java.
    Ces rapports sont générés par le pipeline batch et stockés dans dom_reports/.

    Args:
        file_name: Nom du fichier Java (ex: "LoginPO.java" ou "batch_LoginPO.java.json").

    Returns:
        JSON avec les sélecteurs valides/invalides et les suggestions de correction.
    """
    # Chercher le rapport correspondant
    report_name = file_name.replace(".java", "")
    candidates = [
        REPORTS_DIR / f"batch_{file_name}.json",
        REPORTS_DIR / f"batch_{report_name}.java.json",
        REPORTS_DIR / f"{report_name}.json",
    ]

    for candidate in candidates:
        if candidate.exists():
            try:
                data = json.loads(candidate.read_text(encoding="utf-8"))
                return json.dumps({
                    "found": True,
                    "report_file": candidate.name,
                    "data": data,
                }, ensure_ascii=False, indent=2)
            except Exception as e:
                return json.dumps({"found": True, "error": f"Lecture échouée : {e}"})

    # Lister les rapports disponibles
    available = [f.name for f in REPORTS_DIR.glob("batch_*.json")]
    return json.dumps({
        "found": False,
        "requested": file_name,
        "available_reports": sorted(available)[:20],
        "hint": "Utilisez analyze_page_objects pour générer un rapport.",
    }, ensure_ascii=False, indent=2)


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    mcp.run(transport="stdio")
