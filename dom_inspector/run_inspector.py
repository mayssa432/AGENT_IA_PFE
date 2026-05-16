import argparse
import json
import os
import sys

# Ajouter le répertoire parent au sys.path pour les imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dom_inspector.dom_inspector import DomInspector


def parse_capabilities(path: str) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Fichier de capabilities introuvable : {path}")
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(
        description="Capture et analyse du DOM mobile via Appium"
    )
    parser.add_argument(
        "--capabilities",
        required=True,
        help="Chemin vers un fichier JSON des capacités Appium"
    )
    parser.add_argument(
        "--output",
        default="dom_snapshots",
        help="Répertoire de sortie des snapshots"
    )
    parser.add_argument(
        "--name",
        default=None,
        help="Nom du snapshot"
    )
    parser.add_argument(
        "--server",
        default=os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723"),
        help="URL du serveur Appium"
    )
    parser.add_argument(
        "--java",
        help="Chemin vers un fichier Page Object Java à valider/corriger"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Valide les sélecteurs du fichier Java contre le DOM capturé"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Corrige automatiquement les sélecteurs invalides du fichier Java"
    )
    parser.add_argument(
        "--report-dir",
        default="dom_reports",
        help="Répertoire de sortie pour le rapport JSON"
    )
    args = parser.parse_args()

    capabilities = parse_capabilities(args.capabilities)
    inspector = DomInspector(appium_server_url=args.server, output_dir=args.output)

    snapshot = inspector.capture_dom(capabilities, snapshot_name=args.name)
    print(snapshot.summary())
    print(f"Snapshot XML sauvegardé : {snapshot.path}")
    print(f"Metadata : {snapshot.metadata}")

    root = inspector.parse_snapshot(snapshot.xml)
    print(f"Racine DOM : {root.tag}, éléments : {len(root.xpath('//*'))}")

    if args.validate or args.fix:
        if not args.java:
            raise ValueError("Le chemin du fichier Java est requis pour valider ou corriger des sélecteurs.")
        if not os.path.exists(args.java):
            raise FileNotFoundError(f"Fichier Java introuvable : {args.java}")

    if args.validate:
        issues = inspector.validate_page_object(args.java, root)
        if not issues:
            print(f"✅ Tous les sélecteurs sont valides dans {args.java}")
        else:
            print(f"❌ Sélecteurs invalides détectés dans {args.java} :")
            for issue in issues:
                print(
                    f"Ligne {issue['line']} : {issue['message']}\n"
                    f"  {issue['annotation']}\n"
                )
        report = inspector.generate_validation_report(args.java, root)
        report_path = inspector.save_validation_report(report, f"validation_{os.path.basename(args.java)}")
        print(f"Rapport de validation sauvegardé : {report_path}")

    if args.fix:
        result = inspector.fix_page_object(args.java, root)
        if result.get("success"):
            print(f"✅ Correction terminée pour {result.get('file')}")
            print(f"Corrections appliquées : {result.get('corrections_count')}")
            if result.get("backup"):
                print(f"Sauvegarde : {result.get('backup')}")
            for correction in result.get("corrections", []):
                print(
                    f"Ligne {correction['line']}\n"
                    f"  Avant : {correction['original']}\n"
                    f"  Après  : {correction['fixed']}\n"
                )
        else:
            print(f"Erreur : {result.get('error')}")
        report = inspector.generate_validation_report(args.java, root)
        report_path = inspector.save_validation_report(report, f"validation_{os.path.basename(args.java)}")
        print(f"Rapport de validation sauvegardé : {report_path}")

    if not args.validate and not args.fix:
        if root.xpath('//*[@resource-id]'):
            print("Exemple élément resource-id :")
            target = root.xpath('//*[@resource-id]')[0]
            print(inspector.suggest_selectors(target))


if __name__ == "__main__":
    main()
