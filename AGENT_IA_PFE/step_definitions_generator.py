# -*- coding: utf-8 -*-
import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """Tu es un expert en test automation BDD/Cucumber et Java/Appium.
Tu generes des Step Definitions Java completes a partir de fichiers Gherkin .feature.
Regles :
- Utilise les annotations @Given, @When, @Then, @And de Cucumber
- Importe : io.cucumber.java.en.*, org.junit.Assert, les Page Objects necessaires
- Le package doit etre : com.orange.otvp.automation.steps
- Chaque step doit avoir une implementation basique (commentaire + action)
- Reponds UNIQUEMENT avec le code Java. Commence par package com.orange.otvp.automation.steps;
"""


class StepDefinitionsGenerator:

    def __init__(self, model=None):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = model or os.getenv("MODEL", "llama-3.3-70b-versatile")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY manquante")
        self.client = Groq(api_key=self.api_key)
        print(f"[AGENT] Groq initialise (modele: {self.model})")

    def generate_steps(self, feature_content, page_name):
        prompt = f"""Voici le fichier Gherkin pour la page {page_name}:

{feature_content}

Genere les Step Definitions Java COMPLETES pour ce fichier feature.
Le nom de la classe doit etre : {page_name}Steps
"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2048
        )
        return response.choices[0].message.content.strip()

    def generate_with_retry(self, feature_content, page_name, max_retries=3):
        for attempt in range(max_retries):
            try:
                print(f"  [GROQ] Tentative {attempt+1}/{max_retries}...")
                result = self.generate_steps(feature_content, page_name)
                if "package" in result and "@Given" in result or "@When" in result or "@Then" in result:
                    print("  [GROQ] Generation reussie !")
                    return result
                print("  [GROQ] Format invalide, retry...")
            except Exception as e:
                print(f"  [GROQ] Erreur: {e}")
        raise ValueError(f"Echec apres {max_retries} tentatives")


# ─── MAIN ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    FEATURES_DIR = os.getenv(
        "OUTPUT_DIR",
        r"C:\Users\m.derwich\Downloads\AGENT_IA_PFE\AGENT_IA_PFE\output\features"
    )
    STEPS_DIR = str(Path(FEATURES_DIR).parent / "steps")

    # Créer le dossier steps
    Path(STEPS_DIR).mkdir(parents=True, exist_ok=True)

    generator = StepDefinitionsGenerator()

    feature_files = list(Path(FEATURES_DIR).glob("*.feature"))
    print(f"\n[INFO] {len(feature_files)} fichiers .feature trouvés\n")

    success = 0
    errors = 0

    for feature_file in feature_files:
        page_name = feature_file.stem
        print(f"[PROCESSING] {feature_file.name} -> {page_name}Steps.java...")

        try:
            content = feature_file.read_text(encoding="utf-8")
            result = generator.generate_with_retry(content, page_name)

            # Nettoyer les balises markdown si présentes
            result = result.replace("```java", "").replace("```", "").strip()

            # Sauvegarder
            output_file = Path(STEPS_DIR) / f"{page_name}Steps.java"
            output_file.write_text(result, encoding="utf-8")
            print(f"  [OK] Sauvegarde : {output_file.name}\n")
            success += 1

        except Exception as e:
            print(f"  [ERREUR] {feature_file.name} : {e}\n")
            errors += 1

    print("=" * 50)
    print(f"[RÉSUMÉ] {success} fichiers générés | {errors} erreurs")
    print(f"[OUTPUT] {STEPS_DIR}")
    print("=" * 50)
