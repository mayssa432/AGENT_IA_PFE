"""
demo_mock_manager.py — Démo du pipeline Mock Manager (Livrable #3 PFE)

Pipeline complet :
  1. Simulation d'une réponse API réelle (ou appel HTTP réel si --url fourni)
  2. Chargement du mock WireMock existant (fichier JSON local ou WireMock live)
  3. Diff sémantique réel vs mock (deepdiff)
  4. Mise à jour automatique du mock si différences détectées
  5. Versionnement du mock (backup avant écrasement)
  6. Rapport JSON + résumé console

Usage :
    venv\\Scripts\\python.exe demo_mock_manager.py
    venv\\Scripts\\python.exe demo_mock_manager.py --url https://api.example.com/endpoint
    venv\\Scripts\\python.exe demo_mock_manager.py --mocks-dir ./my_mappings/
"""

import argparse
import copy
import json
import os
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))

# ---------------------------------------------------------------------------
# Import deepdiff (avec fallback gracieux)
# ---------------------------------------------------------------------------
try:
    from deepdiff import DeepDiff
    _HAS_DEEPDIFF = True
except ImportError:
    _HAS_DEEPDIFF = False
    print("[WARN] deepdiff non installé — diff basique utilisé. "
          "Installez : venv\\Scripts\\pip install deepdiff")

# ---------------------------------------------------------------------------
# Données de démo — mock "original" simulant WireMock
# ---------------------------------------------------------------------------
DEMO_MOCK_ORIGINAL = {
    "id": "mock-live-001",
    "request": {
        "method": "GET",
        "url": "/api/v1/live/channels"
    },
    "response": {
        "status": 200,
        "jsonBody": {
            "channels": [
                {"id": "ch1", "name": "TF1", "logo": "tf1.png", "position": 1},
                {"id": "ch2", "name": "France 2", "logo": "f2.png", "position": 2},
                {"id": "ch3", "name": "M6", "logo": "m6_old.png", "position": 3}
            ],
            "total": 3,
            "version": "1.0"
        },
        "headers": {"Content-Type": "application/json"}
    }
}

# Réponse API réelle simulée — contient des changements :
# - logo M6 mis à jour
# - nouvelle chaîne ajoutée
# - version bumped
DEMO_REAL_API_RESPONSE = {
    "url": "/api/v1/live/channels",
    "method": "GET",
    "status_code": 200,
    "response_body": {
        "channels": [
            {"id": "ch1", "name": "TF1", "logo": "tf1.png", "position": 1},
            {"id": "ch2", "name": "France 2", "logo": "f2_hd.png", "position": 2},
            {"id": "ch3", "name": "M6", "logo": "m6_new.png", "position": 3},
            {"id": "ch4", "name": "Canal+", "logo": "canalplus.png", "position": 4}
        ],
        "total": 4,
        "version": "1.2"
    }
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sep(title: str = "") -> None:
    print(f"\n{'─' * 60}")
    if title:
        print(f"  {title}")
        print(f"{'─' * 60}")


def _ok(msg: str) -> None:
    print(f"  ✅  {msg}")


def _fail(msg: str) -> None:
    print(f"  ❌  {msg}")


def _info(msg: str) -> None:
    print(f"  ℹ️   {msg}")


def _semantic_diff(mock_body: dict, real_body: dict) -> dict:
    """Diff sémantique entre mock et réponse réelle."""
    if _HAS_DEEPDIFF:
        diff = DeepDiff(mock_body, real_body, ignore_order=True)
        return diff.to_dict() if diff else {}
    # Fallback JSON string diff
    old_str = json.dumps(mock_body, sort_keys=True, indent=2)
    new_str = json.dumps(real_body, sort_keys=True, indent=2)
    if old_str == new_str:
        return {}
    return {"raw_diff": "bodies differ (deepdiff not available)"}


def _save_mock_version(mock: dict, versions_dir: str) -> str:
    """Sauvegarde une version du mock avant écrasement."""
    os.makedirs(versions_dir, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    mock_id = mock.get("id", "unknown")
    path = os.path.join(versions_dir, f"{mock_id}_{ts}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(mock, f, ensure_ascii=False, indent=2)
    return path


def _print_diff_summary(diff: dict) -> None:
    """Affiche un résumé lisible du diff."""
    if not diff:
        return
    for change_type, changes in diff.items():
        label = {
            "type_changes": "Type changé",
            "values_changed": "Valeur modifiée",
            "dictionary_item_added": "Champ ajouté",
            "dictionary_item_removed": "Champ supprimé",
            "iterable_item_added": "Élément ajouté",
            "iterable_item_removed": "Élément supprimé",
        }.get(change_type, change_type)

        if isinstance(changes, dict):
            for path, detail in list(changes.items())[:5]:
                if isinstance(detail, dict):
                    old = detail.get("old_value", "?")
                    new = detail.get("new_value", "?")
                    print(f"       [{label}] {path}")
                    print(f"         ancien : {str(old)[:60]}")
                    print(f"         nouveau: {str(new)[:60]}")
                else:
                    print(f"       [{label}] {path} : {str(detail)[:80]}")
        elif isinstance(changes, set):
            for item in list(changes)[:3]:
                print(f"       [{label}] {str(item)[:80]}")


# ---------------------------------------------------------------------------
# Pipeline principal
# ---------------------------------------------------------------------------

def run_demo(
    api_url: Optional[str],
    mocks_dir: str,
    output_dir: str,
) -> dict:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    versions_dir = os.path.join(output_dir, "mock_versions")

    print(f"\n{'═' * 60}")
    print(f"  🤖  DÉMO MOCK MANAGER — PFE Livrable #3")
    print(f"  Run : {run_id}")
    print(f"{'═' * 60}")

    results = {"run_id": run_id, "comparisons": [], "summary": {}}

    # ------------------------------------------------------------------
    # ÉTAPE 1 — Charger ou simuler la réponse API réelle
    # ------------------------------------------------------------------
    _sep("ÉTAPE 1 — Réponse API réelle")

    if api_url:
        try:
            import requests
            resp = requests.get(api_url, timeout=10)
            real_response = {
                "url": api_url,
                "method": "GET",
                "status_code": resp.status_code,
                "response_body": resp.json() if resp.headers.get("content-type", "").startswith("application/json") else {"raw": resp.text[:500]},
            }
            _ok(f"Réponse réelle obtenue : {api_url} → HTTP {resp.status_code}")
        except Exception as e:
            _fail(f"Appel API échoué ({e}) — utilisation de la réponse mock de démo.")
            real_response = DEMO_REAL_API_RESPONSE
    else:
        real_response = DEMO_REAL_API_RESPONSE
        _ok("Réponse API simulée utilisée (sans --url).")
        _info(f"URL : {real_response['url']} | Statut : {real_response['status_code']}")
        _info(f"Résumé : {real_response['response_body'].get('total', '?')} chaînes, "
              f"version {real_response['response_body'].get('version', '?')}")

    # ------------------------------------------------------------------
    # ÉTAPE 2 — Charger les mocks existants (fichiers locaux ou WireMock)
    # ------------------------------------------------------------------
    _sep("ÉTAPE 2 — Mocks existants")

    mocks_to_compare: list[dict] = []

    # Essai WireMock live
    try:
        import requests as rq
        wiremock_url = os.getenv("WIREMOCK_URL", "http://localhost:8081")
        resp_wm = rq.get(f"{wiremock_url}/__admin/mappings", timeout=2)
        if resp_wm.status_code == 200:
            mocks_to_compare = resp_wm.json().get("mappings", [])
            _ok(f"WireMock connecté ({wiremock_url}) — {len(mocks_to_compare)} mapping(s) chargé(s).")
    except Exception:
        pass

    # Fallback : fichiers JSON locaux
    if not mocks_to_compare and os.path.isdir(mocks_dir):
        for fname in os.listdir(mocks_dir):
            if fname.endswith(".json"):
                try:
                    with open(os.path.join(mocks_dir, fname), "r", encoding="utf-8") as f:
                        mocks_to_compare.append(json.load(f))
                except Exception:
                    pass
        if mocks_to_compare:
            _ok(f"{len(mocks_to_compare)} mock(s) chargé(s) depuis : {mocks_dir}")

    # Fallback final : mock de démo embarqué
    if not mocks_to_compare:
        mocks_to_compare = [DEMO_MOCK_ORIGINAL]
        _ok("Mock de démo embarqué utilisé.")
        _info(f"Mock ID : {DEMO_MOCK_ORIGINAL['id']} | URL : {DEMO_MOCK_ORIGINAL['request']['url']}")
        _info(f"Résumé : {len(DEMO_MOCK_ORIGINAL['response']['jsonBody']['channels'])} chaînes, "
              f"version {DEMO_MOCK_ORIGINAL['response']['jsonBody']['version']}")

    # ------------------------------------------------------------------
    # ÉTAPE 3 — Diff sémantique
    # ------------------------------------------------------------------
    _sep("ÉTAPE 3 — Diff sémantique réel vs mock")

    updated_count = 0
    unchanged_count = 0

    for mock in mocks_to_compare:
        mock_url = mock.get("request", {}).get("url", "")
        mock_method = mock.get("request", {}).get("method", "GET")
        real_url = real_response.get("url", "")
        real_method = real_response.get("method", "GET")

        # Matcher URL / méthode
        if mock_url not in real_url and real_url not in mock_url:
            _info(f"Mock {mock.get('id','?')} ignoré (URL différente : {mock_url})")
            continue
        if mock_method.upper() != real_method.upper():
            _info(f"Mock {mock.get('id','?')} ignoré (méthode différente)")
            continue

        mock_body = mock.get("response", {}).get("jsonBody", {})
        real_body = real_response.get("response_body", {})
        mock_status = mock.get("response", {}).get("status", 200)
        real_status = real_response.get("status_code", 200)

        diff = _semantic_diff(mock_body, real_body)
        status_mismatch = (mock_status != real_status)
        has_diff = bool(diff) or status_mismatch

        comp = {
            "mock_id": mock.get("id"),
            "url": mock_url,
            "method": mock_method,
            "has_differences": has_diff,
            "status_mismatch": status_mismatch,
            "diff": diff,
        }
        results["comparisons"].append(comp)

        if not has_diff:
            _ok(f"Mock {mock.get('id','?')} [{mock_url}] → aucune différence")
            unchanged_count += 1
            continue

        _fail(f"Mock {mock.get('id','?')} [{mock_url}] → différences détectées !")
        if status_mismatch:
            print(f"       Statut HTTP : mock={mock_status} → réel={real_status}")
        if diff:
            _print_diff_summary(diff)

        # ------------------------------------------------------------------
        # ÉTAPE 4 — Mise à jour automatique
        # ------------------------------------------------------------------
        print(f"\n  → Mise à jour automatique en cours...")

        # Backup versionné
        backup_path = _save_mock_version(mock, versions_dir)
        _ok(f"Backup versionné : {backup_path}")

        # Construire le mock mis à jour
        updated_mock = copy.deepcopy(mock)
        updated_mock["response"]["jsonBody"] = real_body
        updated_mock["response"]["status"] = real_status
        updated_mock["_updated_at"] = datetime.now(timezone.utc).isoformat()
        updated_mock["_previous_version"] = backup_path

        # Tenter WireMock live
        wm_updated = False
        mock_id = mock.get("id")
        if mock_id:
            try:
                import requests as rq
                wm_url = os.getenv("WIREMOCK_URL", "http://localhost:8081")
                payload = {
                    "request": updated_mock["request"],
                    "response": updated_mock["response"],
                }
                resp_put = rq.put(f"{wm_url}/__admin/mappings/{mock_id}", json=payload, timeout=3)
                if resp_put.status_code == 200:
                    _ok(f"WireMock mis à jour (PUT /{mock_id}) → HTTP 200")
                    wm_updated = True
            except Exception:
                pass

        # Fallback : sauvegarder le mock mis à jour localement
        if not wm_updated:
            os.makedirs(mocks_dir, exist_ok=True)
            updated_path = os.path.join(mocks_dir, f"{mock_id or 'mock'}_updated.json")
            with open(updated_path, "w", encoding="utf-8") as f:
                json.dump(updated_mock, f, ensure_ascii=False, indent=2)
            _ok(f"Mock mis à jour sauvegardé localement : {updated_path}")

        updated_count += 1
        comp["updated"] = True
        comp["backup"] = backup_path

    # ------------------------------------------------------------------
    # ÉTAPE 5 — Rapport final
    # ------------------------------------------------------------------
    _sep("ÉTAPE 5 — Rapport")

    results["summary"] = {
        "total_mocks_compared": updated_count + unchanged_count,
        "updated": updated_count,
        "unchanged": unchanged_count,
    }

    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, f"mock_sync_{run_id}.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=str)

    _ok(f"Rapport JSON : {report_path}")

    s = results["summary"]
    print(f"""
╔══════════════════════════════════════════╗
║  ✅  Mock Manager terminé — run {run_id}
║──────────────────────────────────────────
║  Mocks comparés  : {s['total_mocks_compared']}
║  Mocks mis à jour: {s['updated']}
║  Mocks inchangés : {s['unchanged']}
╚══════════════════════════════════════════╝
""")

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Démo Mock Manager — diff réel vs mock + mise à jour auto (PFE Livrable #3)"
    )
    parser.add_argument("--url", help="URL de l'API réelle à appeler (ex: https://api.example.com/endpoint)")
    parser.add_argument("--mocks-dir", default="mock_manager/mappings", help="Dossier des mappings WireMock JSON")
    parser.add_argument("--output-dir", default="output/reports", help="Dossier de sortie rapports")
    args = parser.parse_args()

    run_demo(
        api_url=args.url,
        mocks_dir=args.mocks_dir,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()
