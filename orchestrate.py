"""
orchestrate.py — Point d'entrée unique du pipeline agent IA PFE.

Enchaîne :
  1. App Manager   : détection device / installation APK
  2. DOM Inspector : capture DOM + parsing
  3. Selector Fixer: détection sélecteurs cassés + corrections auto
  4. Rapport       : JSON + résumé console

Usage :
    python orchestrate.py --apk path/to/app.apk --pages path/to/pages/ [options]

Options :
    --apk           Chemin vers l'APK à installer (optionnel si l'app est déjà installée)
    --package       Package Android de l'application (ex: com.example.app)
    --activity      Activité principale à lancer (ex: .MainActivity)
    --pages         Dossier contenant les fichiers Java Page Objects à analyser
    --appium-url    URL du serveur Appium (défaut: http://127.0.0.1:4723)
    --device        Serial du device Android (optionnel — prend le premier disponible)
    --snapshot-dir  Dossier de sauvegarde des snapshots DOM (défaut: dom_snapshots/)
    --report-dir    Dossier de sortie du rapport (défaut: output/reports/)
    --no-fix        Analyse uniquement, sans écrire les corrections dans les fichiers
    --dry-run       Simule tout sans connexion Appium ni device réel
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Imports internes (avec fallback gracieux si dépendance manquante)
# ---------------------------------------------------------------------------
try:
    from app_manager.device_manager import DeviceManager
    from app_manager.app_installer import AppInstaller
    _HAS_APP_MANAGER = True
except ImportError as _e:
    print(f"[WARN] app_manager indisponible : {_e}")
    DeviceManager = None  # type: ignore
    AppInstaller = None   # type: ignore
    _HAS_APP_MANAGER = False

try:
    from dom_inspector.appium_connector import AppiumConnector
    from dom_inspector.dom_capture import DomCapture
    from dom_inspector.ui_parser import UiParser
    from dom_inspector.snapshot_manager import SnapshotManager
    from dom_inspector.selector_fixer import SelectorFixer
    _HAS_DOM_INSPECTOR = True
except ImportError as _e:
    print(f"[WARN] dom_inspector indisponible : {_e}")
    AppiumConnector = DomCapture = UiParser = SnapshotManager = SelectorFixer = None  # type: ignore
    _HAS_DOM_INSPECTOR = False

try:
    from analyzers.xpath_analyzer import XPathAnalyzer
    from analyzers.file_parser import PageObjectParser
    _HAS_ANALYZERS = True
except ImportError as _e:
    print(f"[WARN] analyzers indisponible : {_e}")
    XPathAnalyzer = PageObjectParser = None  # type: ignore
    _HAS_ANALYZERS = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _print_step(num: int, title: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  ÉTAPE {num} — {title}")
    print(f"{'=' * 60}")


def _collect_java_files(pages_dir: str) -> list[str]:
    """Retourne la liste des fichiers Java dans le dossier pages."""
    files = []
    for root, _, filenames in os.walk(pages_dir):
        for fname in filenames:
            if fname.endswith(".java"):
                files.append(os.path.join(root, fname))
    return files


def _build_report(
    run_id: str,
    apk_path: Optional[str],
    device: Optional[str],
    snapshot_path: Optional[str],
    static_issues: list,
    fixer_results: list,
    pages_dir: str,
    report_dir: str,
) -> dict:
    total_fixes = sum(len(r.get("corrections", [])) for r in fixer_results if r.get("success"))
    total_errors = sum(1 for r in fixer_results if not r.get("success"))

    report = {
        "run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input": {
            "apk": apk_path,
            "device": device,
            "pages_dir": pages_dir,
        },
        "dom_snapshot": snapshot_path,
        "summary": {
            "java_files_analysed": len(fixer_results),
            "total_selector_fixes": total_fixes,
            "files_with_errors": total_errors,
            "static_xpath_issues": len(static_issues),
        },
        "static_analysis": [
            {
                "issue_type": getattr(i, "issue_type", str(i)),
                "file": getattr(i, "file", ""),
                "line": getattr(i, "line", 0),
                "message": getattr(i, "message", ""),
                "severity": getattr(i, "severity", ""),
            }
            for i in static_issues
        ],
        "selector_fixes": fixer_results,
    }

    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"report_{run_id}.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)

    # Résumé HTML simple
    html_path = os.path.join(report_dir, f"report_{run_id}.html")
    _write_html_report(report, html_path)

    return {"json": report_path, "html": html_path, "data": report}


def _write_html_report(report: dict, path: str) -> None:
    fixes_rows = ""
    for item in report.get("selector_fixes", []):
        status = "✅ Corrigé" if item.get("success") and item.get("corrections") else (
            "⚠️ Inchangé" if item.get("success") else "❌ Erreur"
        )
        nb = len(item.get("corrections", []))
        fixes_rows += f"<tr><td>{item.get('file','')}</td><td>{nb}</td><td>{status}</td></tr>"

    issues_rows = ""
    for issue in report.get("static_analysis", []):
        issues_rows += (
            f"<tr><td>{issue.get('file','')}</td>"
            f"<td>{issue.get('line',0)}</td>"
            f"<td>{issue.get('severity','')}</td>"
            f"<td>{issue.get('message','')}</td></tr>"
        )

    s = report["summary"]
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Rapport Pipeline Agent IA — {report['run_id']}</title>
  <style>
    body {{ font-family: sans-serif; margin: 2rem; }}
    h1 {{ color: #2c3e50; }}
    h2 {{ color: #34495e; border-bottom: 1px solid #ddd; }}
    table {{ border-collapse: collapse; width: 100%; margin-bottom: 2rem; }}
    th, td {{ border: 1px solid #ccc; padding: 8px 12px; text-align: left; }}
    th {{ background: #f0f4f8; }}
    .badge {{ display:inline-block; padding:2px 8px; border-radius:4px; font-size:.85em; }}
    .ok  {{ background:#d4edda; color:#155724; }}
    .warn{{ background:#fff3cd; color:#856404; }}
    .err {{ background:#f8d7da; color:#721c24; }}
  </style>
</head>
<body>
  <h1>🤖 Rapport Pipeline Agent IA PFE</h1>
  <p><strong>Run ID :</strong> {report['run_id']}</p>
  <p><strong>Date :</strong> {report['timestamp']}</p>
  <p><strong>APK :</strong> {report['input'].get('apk','—')}</p>
  <p><strong>Device :</strong> {report['input'].get('device','—')}</p>

  <h2>📊 Résumé</h2>
  <table>
    <tr><th>Métrique</th><th>Valeur</th></tr>
    <tr><td>Fichiers Java analysés</td><td>{s['java_files_analysed']}</td></tr>
    <tr><td>Sélecteurs corrigés</td><td><span class="badge ok">{s['total_selector_fixes']}</span></td></tr>
    <tr><td>Fichiers en erreur</td><td><span class="badge {'err' if s['files_with_errors'] else 'ok'}">{s['files_with_errors']}</span></td></tr>
    <tr><td>Problèmes XPath statiques</td><td><span class="badge {'warn' if s['static_xpath_issues'] else 'ok'}">{s['static_xpath_issues']}</span></td></tr>
  </table>

  <h2>🔧 Corrections de sélecteurs</h2>
  <table>
    <tr><th>Fichier</th><th>Corrections</th><th>Statut</th></tr>
    {fixes_rows if fixes_rows else '<tr><td colspan="3">Aucune correction appliquée.</td></tr>'}
  </table>

  <h2>⚠️ Problèmes statiques XPath</h2>
  <table>
    <tr><th>Fichier</th><th>Ligne</th><th>Sévérité</th><th>Message</th></tr>
    {issues_rows if issues_rows else '<tr><td colspan="4">Aucun problème détecté.</td></tr>'}
  </table>
</body>
</html>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------

def run_pipeline(
    apk_path: Optional[str],
    package: Optional[str],
    activity: Optional[str],
    pages_dir: str,
    appium_url: str,
    device_serial: Optional[str],
    snapshot_dir: str,
    report_dir: str,
    no_fix: bool,
    dry_run: bool,
) -> dict:

    run_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    print(f"\n🚀 Pipeline Agent IA PFE — run {run_id}")

    snapshot_path: Optional[str] = None
    dom_xml: Optional[str] = None
    ui_root = None
    driver = None

    # ------------------------------------------------------------------
    # ÉTAPE 1 — App Manager : détection device + installation APK
    # ------------------------------------------------------------------
    _print_step(1, "App Manager — Détection device & gestion APK")

    if dry_run:
        print("  [DRY-RUN] Connexion device ignorée.")
        selected_device = device_serial or "emulator-5554"
    elif not _HAS_APP_MANAGER:
        print("  [SKIP] app_manager non disponible (dépendances manquantes).")
        selected_device = device_serial
    else:
        dm = DeviceManager()
        devices = []
        try:
            devices = dm.list_devices()
        except Exception as e:
            print(f"  ⚠️  ADB indisponible : {e}")

        if devices:
            selected_device = device_serial if device_serial in devices else devices[0]
            model = "inconnu"
            try:
                model = dm.get_device_model(selected_device) or "inconnu"
            except Exception:
                pass
            print(f"  ✅ Device sélectionné : {selected_device} ({model})")
        else:
            selected_device = device_serial
            print("  ⚠️  Aucun device Android détecté — étape device ignorée.")

        if apk_path and selected_device:
            installer = AppInstaller()
            try:
                result = installer.install_apk(apk_path, device_serial=selected_device)
                print(f"  ✅ APK installé : {result}")
            except Exception as e:
                print(f"  ❌ Echec installation APK : {e}")

        if package and activity and selected_device:
            installer = AppInstaller()
            try:
                installer.launch_app(package, activity, device_serial=selected_device)
                print(f"  ✅ App lancée : {package}/{activity}")
            except Exception as e:
                print(f"  ⚠️  Echec lancement app : {e}")

    # ------------------------------------------------------------------
    # ÉTAPE 2 — DOM Inspector : capture snapshot DOM
    # ------------------------------------------------------------------
    _print_step(2, "DOM Inspector — Capture DOM & parsing")

    if dry_run:
        print("  [DRY-RUN] Capture DOM ignorée — DOM vide utilisé.")
        dom_xml = "<hierarchy></hierarchy>"
    elif not _HAS_DOM_INSPECTOR:
        print("  [SKIP] dom_inspector non disponible (dépendances manquantes).")
        dom_xml = None
    else:
        caps = {}
        if package:
            caps["appPackage"] = package
        if activity:
            caps["appActivity"] = activity
        if selected_device:
            caps["udid"] = selected_device
        caps["platformName"] = "Android"
        caps["automationName"] = "UiAutomator2"
        caps["noReset"] = True

        connector = AppiumConnector(server_url=appium_url)
        try:
            driver = connector.create_driver(caps)
            capturer = DomCapture()
            dom_xml = capturer.capture_page_source(driver)
            sm = SnapshotManager(base_dir=snapshot_dir)
            snapshot = sm.save(dom_xml, name=f"snapshot_{run_id}", metadata={"run_id": run_id})
            snapshot_path = snapshot.path
            print(f"  ✅ DOM capturé ({len(dom_xml)} chars) → {snapshot_path}")
        except Exception as e:
            print(f"  ❌ Echec capture DOM : {e}")
            print("     ↳ Analyse statique uniquement (sans DOM réel).")
            dom_xml = None
        finally:
            if driver:
                try:
                    connector.close_driver(driver)
                except Exception:
                    pass

    if dom_xml:
        parser = UiParser()
        try:
            ui_root = parser.parse_xml(dom_xml)
            print(f"  ✅ DOM parsé — tag racine : {ui_root.tag}")
        except Exception as e:
            print(f"  ⚠️  Echec parsing XML DOM : {e}")
            ui_root = None

    # ------------------------------------------------------------------
    # ÉTAPE 3 — Analyse statique XPath
    # ------------------------------------------------------------------
    _print_step(3, "Analyzers — Analyse statique des sélecteurs XPath")

    java_files = _collect_java_files(pages_dir)
    print(f"  📁 {len(java_files)} fichier(s) Java trouvé(s) dans : {pages_dir}")

    static_issues = []
    if not _HAS_ANALYZERS:
        print("  [SKIP] analyzers non disponibles (dépendances manquantes).")
    else:
        xpath_analyzer = XPathAnalyzer()
        for jf in java_files:
            try:
                issues = xpath_analyzer.validate(jf)
                static_issues.extend(issues)
            except Exception as e:
                print(f"  ⚠️  Erreur analyse {os.path.basename(jf)}: {e}")

    print(f"  ✅ {len(static_issues)} problème(s) XPath statique(s) détecté(s).")

    # ------------------------------------------------------------------
    # ÉTAPE 4 — Selector Fixer : correction auto dans les Page Objects
    # ------------------------------------------------------------------
    _print_step(4, "Selector Fixer — Correction automatique des sélecteurs")

    fixer_results = []
    if not _HAS_DOM_INSPECTOR:
        print("  [SKIP] SelectorFixer non disponible (dépendances manquantes).")
        for jf in java_files:
            fixer_results.append({"file": jf, "success": False, "error": "dom_inspector non installé", "corrections": []})
    elif ui_root is None:
        print("  ⚠️  Pas de DOM disponible — corrections dynamiques ignorées.")
        for jf in java_files:
            fixer_results.append({"file": jf, "success": False, "error": "DOM non disponible", "corrections": []})
    elif no_fix:
        print("  ℹ️  --no-fix activé — analyse uniquement, aucune écriture.")
        fixer = SelectorFixer()
        for jf in java_files:
            result = fixer.fix_file(jf, ui_root)
            result["file"] = jf
            result["applied"] = False
            fixer_results.append(result)
    else:
        fixer = SelectorFixer()
        for jf in java_files:
            try:
                result = fixer.fix_file(jf, ui_root)
                result["file"] = jf
                nb = len(result.get("corrections", []))
                if nb:
                    print(f"  ✅ {os.path.basename(jf)} : {nb} correction(s) appliquée(s)")
                else:
                    print(f"  — {os.path.basename(jf)} : aucune correction nécessaire")
                fixer_results.append(result)
            except Exception as e:
                print(f"  ❌ Erreur sur {os.path.basename(jf)}: {e}")
                fixer_results.append({"file": jf, "success": False, "error": str(e), "corrections": []})

    total_fixes = sum(len(r.get("corrections", [])) for r in fixer_results)
    print(f"\n  📌 Total corrections appliquées : {total_fixes}")

    # ------------------------------------------------------------------
    # ÉTAPE 5 — Rapport
    # ------------------------------------------------------------------
    _print_step(5, "Rapport — Génération JSON + HTML")

    report_out = _build_report(
        run_id=run_id,
        apk_path=apk_path,
        device=selected_device if not dry_run else None,
        snapshot_path=snapshot_path,
        static_issues=static_issues,
        fixer_results=fixer_results,
        pages_dir=pages_dir,
        report_dir=report_dir,
    )

    print(f"\n  📄 Rapport JSON  : {report_out['json']}")
    print(f"  🌐 Rapport HTML  : {report_out['html']}")

    # Résumé final
    d = report_out["data"]["summary"]
    print(f"""
╔══════════════════════════════════════════╗
║  ✅  Pipeline terminé — run {run_id}
║──────────────────────────────────────────
║  Fichiers analysés      : {d['java_files_analysed']}
║  Sélecteurs corrigés    : {d['total_selector_fixes']}
║  Problèmes XPath static : {d['static_xpath_issues']}
║  Fichiers en erreur     : {d['files_with_errors']}
╚══════════════════════════════════════════╝
""")

    return report_out


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Agent IA PFE — pipeline end-to-end de maintenance des tests mobiles"
    )
    parser.add_argument("--apk", help="Chemin vers l'APK à installer")
    parser.add_argument("--package", help="Package Android (ex: com.example.app)")
    parser.add_argument("--activity", help="Activité principale (ex: .MainActivity)")
    parser.add_argument("--pages", required=True, help="Dossier des Page Objects Java")
    parser.add_argument("--appium-url", default="http://127.0.0.1:4723", help="URL serveur Appium")
    parser.add_argument("--device", help="Serial du device Android")
    parser.add_argument("--snapshot-dir", default="dom_snapshots", help="Dossier snapshots DOM")
    parser.add_argument("--report-dir", default="output/reports", help="Dossier rapports")
    parser.add_argument("--no-fix", action="store_true", help="Analyse uniquement, sans écriture")
    parser.add_argument("--dry-run", action="store_true", help="Simulation sans device ni Appium")

    args = parser.parse_args()

    run_pipeline(
        apk_path=args.apk,
        package=args.package,
        activity=args.activity,
        pages_dir=args.pages,
        appium_url=args.appium_url,
        device_serial=args.device,
        snapshot_dir=args.snapshot_dir,
        report_dir=args.report_dir,
        no_fix=args.no_fix,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
