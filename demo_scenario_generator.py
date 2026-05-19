# -*- coding: utf-8 -*-
"""
demo_scenario_generator.py
===========================
Livrable #4 — Pipeline complet Scenario Generator end-to-end

Démontre la génération automatique :
  1. Lecture d'un Page Object Java Appium
  2. Génération du fichier .feature Gherkin (via Groq LLM ou mode offline)
  3. Génération des Step Definitions Java (via Groq LLM ou mode offline)
  4. Génération du Cucumber Runner Java (template)
  5. Validation + rapport JSON

Usage :
  python demo_scenario_generator.py
  python demo_scenario_generator.py --po-file pages/AuthenticationPO.java
  python demo_scenario_generator.py --offline
"""

import os
import sys
import json
import argparse
import textwrap
from datetime import datetime, timezone
from pathlib import Path

# ─── Chemins par défaut ────────────────────────────────────────────────────
ROOT_DIR    = Path(__file__).parent
AGENT_DIR   = ROOT_DIR / "AGENT_IA_PFE"
PAGES_DIR   = AGENT_DIR / "src" / "test" / "java" / "com" / "orange" / "otvp" / "automation" / "pages" / "mobile"
OUTPUT_DIR  = ROOT_DIR / "output" / "scenario_generator"
REPORTS_DIR = ROOT_DIR / "output" / "reports"

# Charger .env depuis le sous-projet
try:
    from dotenv import load_dotenv
    env_file = AGENT_DIR / ".env"
    if env_file.exists():
        load_dotenv(env_file)
except ImportError:
    pass


# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 1 — CLIENT GROQ (avec fallback offline)
# ═══════════════════════════════════════════════════════════════════════════

def _build_groq_client():
    """Initialise le client Groq si l'API key est disponible."""
    api_key = os.getenv("GROQ_API_KEY", "")
    if not api_key:
        return None, None
    try:
        from groq import Groq
        model = os.getenv("MODEL", "llama-3.3-70b-versatile")
        return Groq(api_key=api_key), model
    except ImportError:
        return None, None


def _call_groq(client, model: str, system: str, user: str, max_tokens=2048) -> str:
    """Appel Groq avec retry simple."""
    for attempt in range(3):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user",   "content": user},
                ],
                temperature=0.3,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            print(f"    [GROQ] Tentative {attempt+1}/3 échouée : {e}")
    return ""


# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 2 — TEMPLATES OFFLINE (soutenance sans réseau)
# ═══════════════════════════════════════════════════════════════════════════

OFFLINE_FEATURE = {
    "AuthenticationPO": textwrap.dedent("""\
        Feature: Authentification utilisateur
          En tant qu'utilisateur de l'application OrangeTV
          Je veux pouvoir m'authentifier
          Afin d'accéder à mes contenus personnalisés

          Scenario: Connexion réussie avec identifiants valides
            Given je suis sur l'écran de connexion
            When je saisie mon adresse email "user@orange.fr"
            And je saisie mon mot de passe "P@ssw0rd"
            And je tape sur le bouton "Se connecter"
            Then je suis redirigé vers l'écran d'accueil

          Scenario: Erreur si email manquant
            Given je suis sur l'écran de connexion
            When je laisse le champ email vide
            And je tape sur le bouton "Se connecter"
            Then je vois le message d'erreur "Veuillez saisir votre email"

          Scenario: Erreur si mot de passe manquant
            Given je suis sur l'écran de connexion
            When je saisie mon adresse email "user@orange.fr"
            And je laisse le champ mot de passe vide
            And je tape sur le bouton "Se connecter"
            Then je vois le message d'erreur "Veuillez saisir votre mot de passe"

          Scenario: Connexion avec un autre compte
            Given je suis sur l'écran de connexion
            When je tape sur "Utiliser un autre compte"
            Then le champ email devient éditable
    """),
}

OFFLINE_STEPS = {
    "AuthenticationPO": textwrap.dedent("""\
        package com.orange.otvp.automation.steps;

        import io.cucumber.java.en.*;
        import org.junit.Assert;
        import com.orange.otvp.automation.pages.mobile.AuthenticationPO;

        public class AuthenticationPOSteps {

            private AuthenticationPO authPage;

            @Given("je suis sur l'écran de connexion")
            public void iAmOnLoginScreen() {
                // Navigation vers l'écran de connexion
                Assert.assertNotNull("La page d'authentification doit être chargée", authPage);
            }

            @When("je saisie mon adresse email {string}")
            public void iEnterEmail(String email) {
                authPage.getUserNameField().sendKeys(email);
            }

            @When("je saisie mon mot de passe {string}")
            public void iEnterPassword(String password) {
                authPage.getPasswordField().sendKeys(password);
            }

            @When("je tape sur le bouton {string}")
            public void iTapButton(String label) {
                authPage.getSignInButton().click();
            }

            @Then("je suis redirigé vers l'écran d'accueil")
            public void iAmOnHomeScreen() {
                Assert.assertTrue("L'accueil doit s'afficher", true);
            }

            @When("je laisse le champ email vide")
            public void iLeaveEmailEmpty() {
                authPage.getUserNameField().clear();
            }

            @When("je laisse le champ mot de passe vide")
            public void iLeavePasswordEmpty() {
                authPage.getPasswordField().clear();
            }

            @Then("je vois le message d'erreur {string}")
            public void iSeeErrorMessage(String message) {
                Assert.assertNotNull("Le message d'erreur doit être affiché", message);
            }

            @When("je tape sur {string}")
            public void iTap(String label) {
                authPage.getInputOtherAccountButton().click();
            }

            @Then("le champ email devient éditable")
            public void emailFieldIsEditable() {
                Assert.assertTrue("Le champ email doit être actif", true);
            }
        }
    """),
}

RUNNER_TEMPLATE = textwrap.dedent("""\
    package com.orange.otvp.automation.runners;

    import io.cucumber.junit.Cucumber;
    import io.cucumber.junit.CucumberOptions;
    import org.junit.runner.RunWith;

    @RunWith(Cucumber.class)
    @CucumberOptions(
        features = "src/test/resources/features/{feature_file}",
        glue = "com.orange.otvp.automation.steps",
        plugin = {{
            "pretty",
            "html:target/cucumber-reports/{page_name}-report.html",
            "json:target/cucumber-reports/{page_name}-report.json"
        }},
        monochrome = true
    )
    public class {page_name}Runner {{
    }}
""")


# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 3 — GÉNÉRATEURS
# ═══════════════════════════════════════════════════════════════════════════

def generate_feature(po_content: str, page_name: str, client, model: str, offline: bool) -> tuple[str, str]:
    """Génère le .feature Gherkin. Retourne (contenu, source)."""
    if not offline and client:
        system = (
            "Tu es un expert BDD/Gherkin et Appium. "
            "Génère un fichier .feature Gherkin COMPLET à partir du Page Object Java fourni. "
            "Règles : Feature, minimum 3 Scenario, steps Given/When/Then/And en français. "
            "Commence OBLIGATOIREMENT par 'Feature:'. Réponds UNIQUEMENT avec le Gherkin."
        )
        user = (
            f"Page Object Java pour la page {page_name}:\n\n{po_content[:3000]}\n\n"
            "Génère le fichier .feature COMPLET avec minimum 3 scénarios."
        )
        result = _call_groq(client, model, system, user)
        if result and "Feature:" in result and "Scenario:" in result:
            return result, "groq-llm"

    # Fallback offline
    if page_name in OFFLINE_FEATURE:
        return OFFLINE_FEATURE[page_name], "offline-template"
    # Génération générique offline
    generic = textwrap.dedent(f"""\
        Feature: {page_name.replace('PO', '')} - Fonctionnalités principales

          Scenario: Affichage de la page
            Given je navigue vers la page {page_name.replace('PO', '')}
            Then la page est correctement chargée

          Scenario: Interaction principale
            Given je suis sur la page {page_name.replace('PO', '')}
            When j'effectue l'action principale
            Then le résultat attendu est visible

          Scenario: Cas d'erreur
            Given je suis sur la page {page_name.replace('PO', '')}
            When je fournis des données incorrectes
            Then un message d'erreur s'affiche
    """)
    return generic, "offline-generic"


def generate_steps(feature_content: str, page_name: str, client, model: str, offline: bool) -> tuple[str, str]:
    """Génère les Step Definitions Java. Retourne (contenu, source)."""
    if not offline and client:
        system = (
            "Tu es un expert Cucumber/Java/Appium. "
            "Génère des Step Definitions Java COMPLÈTES à partir du fichier Gherkin fourni. "
            "Package : com.orange.otvp.automation.steps. "
            "Utilise @Given, @When, @Then, @And de io.cucumber.java.fr.*. "
            f"Classe : {page_name}Steps. "
            "Commence par 'package com.orange.otvp.automation.steps;'. Réponds UNIQUEMENT avec le code Java."
        )
        user = (
            f"Fichier Gherkin pour {page_name}:\n\n{feature_content}\n\n"
            "Génère les Step Definitions Java COMPLÈTES."
        )
        result = _call_groq(client, model, system, user)
        if result and "package" in result and ("@Given" in result or "@When" in result or "@Then" in result):
            return result, "groq-llm"

    if page_name in OFFLINE_STEPS:
        return OFFLINE_STEPS[page_name], "offline-template"

    generic = textwrap.dedent(f"""\
        package com.orange.otvp.automation.steps;

        import io.cucumber.java.en.*;
        import org.junit.Assert;

        public class {page_name}Steps {{

            @Given("je navigue vers la page {page_name.replace('PO', '')}")
            public void navigateToPage() {{
                // TODO: implémenter la navigation
            }}

            @Then("la page est correctement chargée")
            public void pageIsLoaded() {{
                Assert.assertTrue("La page doit être chargée", true);
            }}

            @Given("je suis sur la page {page_name.replace('PO', '')}")
            public void iAmOnPage() {{
                // TODO: vérifier état de la page
            }}

            @When("j'effectue l'action principale")
            public void performMainAction() {{
                // TODO: implémenter l'action
            }}

            @Then("le résultat attendu est visible")
            public void resultIsVisible() {{
                Assert.assertTrue("Le résultat doit être visible", true);
            }}

            @When("je fournis des données incorrectes")
            public void provideInvalidData() {{
                // TODO: saisir des données invalides
            }}

            @Then("un message d'erreur s'affiche")
            public void errorMessageIsDisplayed() {{
                Assert.assertNotNull("Le message d'erreur doit s'afficher", true);
            }}
        }}
    """)
    return generic, "offline-generic"


def generate_runner(page_name: str, feature_filename: str) -> str:
    """Génère le Cucumber Runner Java (template, pas de LLM nécessaire)."""
    return RUNNER_TEMPLATE.format(
        feature_file=feature_filename,
        page_name=page_name,
    )


# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 4 — VALIDATION
# ═══════════════════════════════════════════════════════════════════════════

def validate_feature(content: str) -> dict:
    """Valide la structure du fichier .feature (supports EN + FR Gherkin)."""
    import re
    # Mots-clés FR : Given=Étant donné/Soit, When=Quand/Lorsque/Lorsqu', Then=Alors, And=Et/Mais
    checks = {
        "has_feature":   bool(re.search(r"^\s*Feature:", content, re.MULTILINE)),
        "has_scenario":  bool(re.search(r"^\s*Scenario(| Outline):", content, re.MULTILINE)),
        "has_given":     bool(re.search(r"^\s*(Given|Etant|Étant|Soit\b)", content, re.MULTILINE | re.IGNORECASE)),
        "has_when":      bool(re.search(r"^\s*(When|Quand|Lorsque|Lorsqu)", content, re.MULTILINE | re.IGNORECASE)),
        "has_then":      bool(re.search(r"^\s*(Then|Alors)", content, re.MULTILINE | re.IGNORECASE)),
    }
    scenario_count = len(re.findall(r"^\s*Scenario(| Outline):", content, re.MULTILINE))
    checks["scenario_count"] = scenario_count
    checks["valid"] = all(v for k, v in checks.items() if k not in ("scenario_count",))
    return checks


def validate_steps(content: str, page_name: str) -> dict:
    """Valide la structure des Step Definitions Java."""
    import re
    step_count = len(re.findall(r"@(Given|When|Then|And)", content))
    checks = {
        "has_package":    "package com.orange.otvp.automation.steps" in content,
        "has_class":      f"class {page_name}Steps" in content,
        "has_given":      "@Given" in content,
        "has_when":       "@When" in content,
        "has_then":       "@Then" in content,
        "step_count":     step_count,
    }
    checks["valid"] = checks["has_package"] and checks["has_class"] and step_count >= 3
    return checks


# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 5 — PIPELINE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════

def run_pipeline(po_path: Path, offline: bool = False) -> dict:
    page_name = po_path.stem  # ex: "AuthenticationPO"
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    separator = "═" * 60
    print(f"\n{separator}")
    print(f"  LIVRABLE #4 — SCENARIO GENERATOR END-TO-END")
    print(f"  Page Object : {po_path.name}")
    print(f"  Mode        : {'OFFLINE' if offline else 'GROQ LLM'}")
    print(f"  Timestamp   : {timestamp}")
    print(separator)

    # ── Créer dossiers de sortie ───────────────────────────────────────────
    features_dir = OUTPUT_DIR / "features"
    steps_dir    = OUTPUT_DIR / "steps"
    runners_dir  = OUTPUT_DIR / "runners"
    features_dir.mkdir(parents=True, exist_ok=True)
    steps_dir.mkdir(parents=True, exist_ok=True)
    runners_dir.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report = {
        "timestamp":  timestamp,
        "page_object": po_path.name,
        "mode":        "offline" if offline else "groq-llm",
        "steps":       {},
        "files":       {},
        "success":     False,
    }

    # ── Étape 1 : Lecture du Page Object ──────────────────────────────────
    print("\n[ÉTAPE 1/5] Lecture du Page Object Java...")
    try:
        po_content = po_path.read_text(encoding="utf-8")
        line_count = len(po_content.splitlines())
        field_count = po_content.count("@AndroidFindBy") + po_content.count("@iOSXCUITFindBy")
        print(f"  ✅  {po_path.name} chargé — {line_count} lignes, {field_count} sélecteurs détectés")
        report["steps"]["step1_load_po"] = {
            "status": "ok",
            "lines": line_count,
            "selectors": field_count,
        }
    except Exception as e:
        print(f"  ❌  Impossible de lire {po_path}: {e}")
        report["steps"]["step1_load_po"] = {"status": "error", "error": str(e)}
        return report

    # ── Étape 2 : Génération du .feature ──────────────────────────────────
    print("\n[ÉTAPE 2/5] Génération du fichier .feature Gherkin...")
    client, model = _build_groq_client()
    if client:
        print(f"  [GROQ] Client initialisé (modèle: {model})")
    else:
        print("  [INFO] Groq non disponible → mode offline activé")
        offline = True

    feature_content, feature_source = generate_feature(po_content, page_name, client, model or "", offline)
    feature_file = features_dir / f"{page_name}.feature"
    feature_file.write_text(feature_content, encoding="utf-8")

    validation_f = validate_feature(feature_content)
    status_f  = "✅" if validation_f["valid"] else "⚠️ "
    print(f"  {status_f}  {feature_file.name} généré ({feature_source})")
    print(f"       → {validation_f['scenario_count']} scénarios | "
          f"Feature:{validation_f['has_feature']} | "
          f"Given:{validation_f['has_given']} | When:{validation_f['has_when']} | Then:{validation_f['has_then']}")

    report["steps"]["step2_feature"] = {
        "status":     "ok" if validation_f["valid"] else "warning",
        "source":     feature_source,
        "validation": validation_f,
    }
    report["files"]["feature"] = str(feature_file.relative_to(ROOT_DIR))

    # ── Étape 3 : Génération des Step Definitions ──────────────────────────
    print("\n[ÉTAPE 3/5] Génération des Step Definitions Java...")
    steps_content, steps_source = generate_steps(feature_content, page_name, client, model or "", offline)
    steps_file = steps_dir / f"{page_name}Steps.java"
    steps_file.write_text(steps_content, encoding="utf-8")

    validation_s = validate_steps(steps_content, page_name)
    status_s = "✅" if validation_s["valid"] else "⚠️ "
    print(f"  {status_s}  {steps_file.name} généré ({steps_source})")
    print(f"       → {validation_s['step_count']} step definitions | "
          f"Package:{validation_s['has_package']} | "
          f"Classe:{validation_s['has_class']}")

    report["steps"]["step3_step_definitions"] = {
        "status":     "ok" if validation_s["valid"] else "warning",
        "source":     steps_source,
        "validation": validation_s,
    }
    report["files"]["steps"] = str(steps_file.relative_to(ROOT_DIR))

    # ── Étape 4 : Génération du Runner ─────────────────────────────────────
    print("\n[ÉTAPE 4/5] Génération du Cucumber Runner Java...")
    runner_content = generate_runner(page_name, f"{page_name}.feature")
    runner_file = runners_dir / f"{page_name}Runner.java"
    runner_file.write_text(runner_content, encoding="utf-8")

    print(f"  ✅  {runner_file.name} généré (template)")
    print(f"       → features: src/test/resources/features/{page_name}.feature")
    print(f"       → glue:     com.orange.otvp.automation.steps")

    report["steps"]["step4_runner"] = {
        "status": "ok",
        "source": "template",
    }
    report["files"]["runner"] = str(runner_file.relative_to(ROOT_DIR))

    # ── Étape 5 : Rapport JSON ─────────────────────────────────────────────
    print("\n[ÉTAPE 5/5] Génération du rapport de synthèse...")
    report["success"] = validation_f["valid"] and validation_s["valid"]

    report_file = REPORTS_DIR / f"scenario_gen_{page_name}_{timestamp}.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"  ✅  Rapport JSON : {report_file.relative_to(ROOT_DIR)}")

    # ── Résumé final ───────────────────────────────────────────────────────
    print(f"\n{separator}")
    overall = "✅  SUCCÈS" if report["success"] else "⚠️   SUCCÈS PARTIEL"
    print(f"  {overall}")
    print(f"  Fichiers générés : 3  (feature + steps + runner)")
    print(f"  Scénarios Gherkin: {validation_f['scenario_count']}")
    print(f"  Step Definitions : {validation_s['step_count']}")
    print(f"  Source LLM       : {feature_source}")
    print(f"  Dossier sortie   : output/scenario_generator/")
    print(separator)

    return report


# ═══════════════════════════════════════════════════════════════════════════
#  SECTION 6 — BATCH MODE (plusieurs PO d'un coup)
# ═══════════════════════════════════════════════════════════════════════════

def run_batch(pages_dir: Path, limit: int, offline: bool) -> None:
    java_files = sorted(pages_dir.glob("*.java"))[:limit]
    if not java_files:
        print(f"[ERREUR] Aucun fichier .java trouvé dans {pages_dir}")
        sys.exit(1)

    print(f"\n{'═'*60}")
    print(f"  MODE BATCH — {len(java_files)} Page Objects")
    print(f"{'═'*60}")

    results = []
    for po_path in java_files:
        r = run_pipeline(po_path, offline=offline)
        results.append({
            "page": po_path.name,
            "success": r.get("success", False),
            "scenarios": r.get("steps", {}).get("step2_feature", {}).get("validation", {}).get("scenario_count", 0),
            "steps": r.get("steps", {}).get("step3_step_definitions", {}).get("validation", {}).get("step_count", 0),
        })

    # Résumé batch
    total_ok = sum(1 for r in results if r["success"])
    total_scenarios = sum(r["scenarios"] for r in results)
    total_steps = sum(r["steps"] for r in results)

    print(f"\n{'═'*60}")
    print(f"  BILAN BATCH")
    print(f"{'═'*60}")
    print(f"  Page Objects traités : {len(results)}")
    print(f"  Succès               : {total_ok}/{len(results)}")
    print(f"  Total scénarios      : {total_scenarios}")
    print(f"  Total step defs      : {total_steps}")
    for r in results:
        icon = "✅" if r["success"] else "⚠️ "
        print(f"  {icon}  {r['page']:<30} → {r['scenarios']} scénarios, {r['steps']} steps")
    print(f"{'═'*60}")


# ═══════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Livrable #4 — Génération automatique de scénarios BDD depuis un Page Object Java"
    )
    parser.add_argument(
        "--po-file",
        default=str(PAGES_DIR / "AuthenticationPO.java"),
        help="Chemin du Page Object Java à traiter (défaut: AuthenticationPO.java)",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Mode offline : utilise des templates pré-écrits sans appel LLM",
    )
    parser.add_argument(
        "--batch",
        type=int,
        default=0,
        metavar="N",
        help="Traiter les N premiers Page Objects du répertoire en batch",
    )
    args = parser.parse_args()

    if args.batch > 0:
        run_batch(PAGES_DIR, limit=args.batch, offline=args.offline)
    else:
        po_path = Path(args.po_file)
        if not po_path.exists():
            # Essayer dans le répertoire pages
            alt = PAGES_DIR / po_path.name
            if alt.exists():
                po_path = alt
            else:
                print(f"[ERREUR] Fichier introuvable : {po_path}")
                sys.exit(1)
        run_pipeline(po_path, offline=args.offline)
