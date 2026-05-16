# -*- coding: utf-8 -*-
import os
from pathlib import Path
from dotenv import load_dotenv
from scenario_generator import GherkinToJavaAgent

load_dotenv()

# Chemins
PROJECT_PATH = os.getenv("PROJECT_PATH", r"C:\Users\m.derwich\Downloads\AGENT_IA_PFE\AGENT_IA_PFE\src\test\java\com\orange\otvp\automation\pages\mobile")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", r"C:\Users\m.derwich\Downloads\AGENT_IA_PFE\AGENT_IA_PFE\output\features")

# Créer le dossier output si inexistant
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# Initialiser l'agent
agent = GherkinToJavaAgent()

# Récupérer tous les fichiers Java
java_files = list(Path(PROJECT_PATH).glob("*.java"))
print(f"\n[INFO] {len(java_files)} fichiers Java trouvés\n")

# Générer les scénarios
success = 0
errors = 0

for java_file in java_files:
    page_name = java_file.stem.replace("PO", "")
    print(f"[PROCESSING] {java_file.name} -> {page_name}...")

    try:
        content = java_file.read_text(encoding="utf-8")
        result = agent.generate_with_retry(content, page_name)

        # Sauvegarder le fichier .feature
        output_file = Path(OUTPUT_DIR) / f"{page_name}.feature"
        output_file.write_text(result, encoding="utf-8")
        print(f"  [OK] Sauvegarde : {output_file.name}\n")
        success += 1

    except Exception as e:
        print(f"  [ERREUR] {java_file.name} : {e}\n")
        errors += 1

# Résumé
print("=" * 50)
print(f"[RÉSUMÉ] {success} fichiers générés | {errors} erreurs")
print(f"[OUTPUT] {OUTPUT_DIR}")
print("=" * 50)
