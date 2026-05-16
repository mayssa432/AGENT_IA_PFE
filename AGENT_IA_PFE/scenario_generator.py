# -*- coding: utf-8 -*-
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """Tu es un expert en test automation BDD/Gherkin et Cucumber.
Tu generes des scenarios Gherkin complets a partir de Page Objects Java Appium.
Regles : utilise Feature, Scenario, Given, When, Then, And.
Reponds UNIQUEMENT avec le contenu Gherkin. Commence par Feature:
"""


class GherkinToJavaAgent:

    def __init__(self, model=None):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = model or os.getenv("MODEL", "llama-3.3-70b-versatile")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY manquante")
        self.client = Groq(api_key=self.api_key)
        print(f"[AGENT] Groq initialise (modele: {self.model})")

    def generate_feature(self, content, page_name):
        prompt = f"""Voici le Page Object Java pour la page {page_name}:

{content}

Genere un fichier .feature Gherkin COMPLET avec minimum 3 scenarios."""

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

    def generate_with_retry(self, content, page_name, max_retries=3):
        for attempt in range(max_retries):
            try:
                print(f"  [GROQ] Tentative {attempt+1}/{max_retries}...")
                result = self.generate_feature(content, page_name)
                if "Feature:" in result and "Scenario:" in result:
                    print("  [GROQ] Generation reussie !")
                    return result
                print("  [GROQ] Format invalide, retry...")
            except Exception as e:
                print(f"  [GROQ] Erreur: {e}")
        raise ValueError(f"Echec apres {max_retries} tentatives")
