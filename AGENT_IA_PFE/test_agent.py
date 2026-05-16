"""
test_agent.py - Tests de l'agent sans clé API (mode dry-run / mock)

Usage:
    python test_agent.py
"""

import json
import sys
import os
import shutil

# Ajouter le dossier du projet au path
sys.path.insert(0, os.path.dirname(__file__))

from gherkin_parser import GherkinParser, feature_to_dict
from prompt_builder import build_user_prompt, SYSTEM_PROMPT
from file_writer import JavaFileWriter
from dotenv import load_dotenv

# ── Chemins ─────────────────────────────────────────────
FEATURE_PATH = os.path.join(os.path.dirname(__file__), "examples", "login.feature")
OUTPUT_DIR   = os.path.join(os.path.dirname(__file__), "output_test")

# ── Couleurs console ─────────────────────────────────────
import os as _os
_ANSI  = sys.stdout.isatty() or _os.environ.get("TERM") is not None
GREEN  = "\033[92m" if _ANSI else ""
RED    = "\033[91m" if _ANSI else ""
YELLOW = "\033[93m" if _ANSI else ""
RESET  = "\033[0m"  if _ANSI else ""
BOLD   = "\033[1m"  if _ANSI else ""

# ── Compteurs ────────────────────────────────────────────
passed = 0
failed = 0
warned = 0

# ── Helpers ──────────────────────────────────────────────
def ok(msg: str):
    global passed
    passed += 1
    print(f"  {GREEN}✅ PASS{RESET}  {msg}")

def fail(msg: str, err: str = ""):
    global failed
    failed += 1
    print(f"  {RED}❌ FAIL{RESET}  {msg}")
    if err:
        print(f"         {RED}↳ {err}{RESET}")

def warn(msg: str):
    global warned
    warned += 1
    print(f"  {YELLOW}⚠️  WARN{RESET}  {msg}")

def section(title: str):
    print(f"\n{BOLD}{'─'*55}{RESET}")
    print(f"{BOLD}  {title}{RESET}")
    print(f"{BOLD}{'─'*55}{RESET}")


# ══════════════════════════════════════════════════════════
# TEST 1 : GherkinParser - Lecture du fichier .feature
# ══════════════════════════════════════════════════════════
section("TEST 1 : GherkinParser - Lecture fichier")

# 1.1 - Vérifier que le fichier existe
if os.path.exists(FEATURE_PATH):
    ok(f"Fichier trouvé : examples/login.feature")
else:
    fail(
        "Fichier examples/login.feature introuvable",
        f"Chemin attendu : {FEATURE_PATH}"
    )
    sys.exit(1)

# 1.2 - Parser le fichier
try:
    parser  = GherkinParser()
    feature = parser.parse_file(FEATURE_PATH)
    ok("Fichier .feature parsé sans erreur")
except Exception as e:
    fail("Erreur lors du parsing du fichier .feature", str(e))
    sys.exit(1)

# 1.3 - Vérifier le nom de la feature
if feature.name == "Login functionality":
    ok(f"Feature name = '{feature.name}'")
else:
    fail(
        f"Feature name incorrect",
        f"Attendu : 'Login functionality' | Reçu : '{feature.name}'"
    )

# 1.4 - Vérifier le nombre de scénarios
if len(feature.scenarios) == 2:
    ok(f"Nombre de scénarios = {len(feature.scenarios)}")
else:
    fail(
        "Nombre de scénarios incorrect",
        f"Attendu : 2 | Reçu : {len(feature.scenarios)}"
    )

# 1.5 - Vérifier les steps du scénario 1
expected_steps_s1 = 6
actual_steps_s1   = len(feature.scenarios[0].steps)
if actual_steps_s1 == expected_steps_s1:
    ok(f"Scénario 1 '{feature.scenarios[0].name}' : {actual_steps_s1} steps")
else:
    fail(
        f"Scénario 1 : nombre de steps incorrect",
        f"Attendu : {expected_steps_s1} | Reçu : {actual_steps_s1}"
    )

# 1.6 - Vérifier les steps du scénario 2
expected_steps_s2 = 6
actual_steps_s2   = len(feature.scenarios[1].steps)
if actual_steps_s2 == expected_steps_s2:
    ok(f"Scénario 2 '{feature.scenarios[1].name}' : {actual_steps_s2} steps")
else:
    fail(
        f"Scénario 2 : nombre de steps incorrect",
        f"Attendu : {expected_steps_s2} | Reçu : {actual_steps_s2}"
    )

# 1.7 - Vérifier les keywords du scénario 1
keywords_s1 = [s.keyword for s in feature.scenarios[0].steps]

if keywords_s1[0] == "Given":
    ok(f"Premier keyword = 'Given'")
else:
    fail(
        "Premier keyword incorrect",
        f"Attendu : 'Given' | Reçu : '{keywords_s1[0]}'"
    )

if "When" in keywords_s1:
    ok("Keyword 'When' présent dans le scénario 1")
else:
    fail("Keyword 'When' manquant dans le scénario 1")

if "Then" in keywords_s1:
    ok("Keyword 'Then' présent dans le scénario 1")
else:
    fail("Keyword 'Then' manquant dans le scénario 1")

# 1.8 - Afficher tous les steps pour vérification visuelle
print(f"\n  {BOLD}📋 Steps du Scénario 1 :{RESET}")
for i, step in enumerate(feature.scenarios[0].steps, 1):
    print(f"     {i}. [{step.keyword}] {step.text}")

print(f"\n  {BOLD}📋 Steps du Scénario 2 :{RESET}")
for i, step in enumerate(feature.scenarios[1].steps, 1):
    print(f"     {i}. [{step.keyword}] {step.text}")


# ══════════════════════════════════════════════════════════
# TEST 2 : feature_to_dict - Conversion en dictionnaire
# ══════════════════════════════════════════════════════════
section("TEST 2 : feature_to_dict - Conversion JSON")

# 2.1 - Conversion
try:
    d = feature_to_dict(feature)
    ok("feature_to_dict() exécuté sans erreur")
except Exception as e:
    fail("feature_to_dict() a levé une exception", str(e))
    d = {}

# 2.2 - Vérifier les clés requises
required_keys = ["feature_name", "description", "tags", "scenarios"]
for k in required_keys:
    if k in d:
        ok(f"Clé '{k}' présente dans le dict")
    else:
        fail(f"Clé '{k}' manquante dans le dict")

# 2.3 - Vérifier la sérialisation JSON
try:
    json_str = json.dumps(d, ensure_ascii=False, indent=2)
    ok(f"Dict sérialisable en JSON ({len(json_str)} caractères)")
except Exception as e:
    fail("Sérialisation JSON échouée", str(e))

# 2.4 - Vérifier le contenu du dict
if d.get("feature_name") == "Login functionality":
    ok("feature_name correct dans le dict")
else:
    fail(
        "feature_name incorrect dans le dict",
        f"Reçu : '{d.get('feature_name')}'"
    )

if isinstance(d.get("scenarios"), list) and len(d["scenarios"]) == 2:
    ok(f"scenarios : liste de {len(d['scenarios'])} éléments")
else:
    fail("scenarios : format incorrect dans le dict")


# ══════════════════════════════════════════════════════════
# TEST 3 : PromptBuilder - Construction du prompt
# ══════════════════════════════════════════════════════════
section("TEST 3 : PromptBuilder - Construction du prompt")

# 3.1 - Build du prompt
try:
    prompt = build_user_prompt(feature)
    ok("build_user_prompt() exécuté sans erreur")
except Exception as e:
    fail("build_user_prompt() a levé une exception", str(e))
    prompt = ""

# 3.2 - Vérifier le contenu du prompt
checks = {
    "Login functionality"            : "Feature name présent dans le prompt",
    "Successful login"               : "Nom du scénario 1 présent dans le prompt",
    "Failed login with wrong credentials" : "Nom du scénario 2 présent dans le prompt",
    "Given"                          : "Keyword 'Given' présent dans le prompt",
    "When"                           : "Keyword 'When' présent dans le prompt",
    "Then"                           : "Keyword 'Then' présent dans le prompt",
}

for keyword, message in checks.items():
    if keyword in prompt:
        ok(message)
    else:
        fail(f"{message} → '{keyword}' introuvable")

# 3.3 - Vérifier le SYSTEM_PROMPT
if len(SYSTEM_PROMPT) > 100:
    ok(f"SYSTEM_PROMPT défini ({len(SYSTEM_PROMPT)} caractères)")
else:
    fail(
        "SYSTEM_PROMPT trop court ou vide",
        f"Longueur actuelle : {len(SYSTEM_PROMPT)} chars"
    )

# 3.4 - Vérifier la longueur du prompt utilisateur
if len(prompt) > 50:
    ok(f"Prompt utilisateur non vide ({len(prompt)} caractères)")
else:
    fail("Prompt utilisateur trop court ou vide")


# ══════════════════════════════════════════════════════════
# TEST 4 : JavaFileWriter - Génération des fichiers
# ══════════════════════════════════════════════════════════
section("TEST 4 : JavaFileWriter - Génération fichiers Java")

mock_generated = {
    "feature_file": {
        "filename": "src/test/resources/features/login.feature",
        "content" : (
            "Feature: Login functionality\n"
            "  Scenario: Successful login\n"
            "    Given I am on the login page\n"
            "    When I enter username \"admin\"\n"
            "    Then I should be redirected to the dashboard"
        )
    },
    "step_definitions": {
        "filename": "src/test/java/steps/LoginStepDefinitions.java",
        "content" : (
            "package steps;\n\n"
            "import io.cucumber.java.en.*;\n\n"
            "public class LoginStepDefinitions {\n\n"
            "    @Given(\"I am on the login page\")\n"
            "    public void iAmOnTheLoginPage() {\n"
            "        // TODO: implement\n"
            "    }\n"
            "}"
        )
    },
    "page_object": {
        "filename": "src/test/java/pages/LoginPage.java",
        "content" : (
            "package pages;\n\n"
            "public class LoginPage extends BasePage {\n\n"
            "    public void enterUsername(String username) {\n"
            "        // TODO: implement\n"
            "    }\n"
            "}"
        )
    },
    "base_page": {
        "filename": "src/test/java/pages/BasePage.java",
        "content" : (
            "package pages;\n\n"
            "import org.openqa.selenium.WebDriver;\n\n"
            "public class BasePage {\n\n"
            "    protected WebDriver driver;\n\n"
            "    public BasePage(WebDriver driver) {\n"
            "        this.driver = driver;\n"
            "    }\n"
            "}"
        )
    },
    "runner": {
        "filename": "src/test/java/runners/LoginTestRunner.java",
        "content" : (
            "package runners;\n\n"
            "import io.cucumber.junit.Cucumber;\n"
            "import org.junit.runner.RunWith;\n\n"
            "@RunWith(Cucumber.class)\n"
            "public class LoginTestRunner {\n"
            "}"
        )
    }
}

# 4.1 - Créer le writer et écrire les fichiers
try:
    writer  = JavaFileWriter(OUTPUT_DIR)
    written = writer.write_all(mock_generated)
    ok(f"JavaFileWriter : {len(written)} fichier(s) créé(s)")
except Exception as e:
    fail("JavaFileWriter.write_all() a levé une exception", str(e))
    written = []

# 4.2 - Vérifier le nombre de fichiers
expected_count = 5
if len(written) == expected_count:
    ok(f"Nombre de fichiers générés = {expected_count}")
else:
    fail(
        "Nombre de fichiers incorrect",
        f"Attendu : {expected_count} | Reçu : {len(written)}"
    )

# 4.3 - Vérifier que chaque fichier existe sur le disque
for filepath in written:
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        ok(f"Fichier créé : {os.path.basename(filepath)} ({size} bytes)")
    else:
        fail(f"Fichier manquant sur le disque : {filepath}")

# 4.4 - Vérifier les extensions des fichiers
java_files    = [f for f in written if f.endswith(".java")]
feature_files = [f for f in written if f.endswith(".feature")]

if len(java_files) == 4:
    ok(f"4 fichiers Java générés")
else:
    fail(f"Attendu 4 fichiers .java | Reçu : {len(java_files)}")

if len(feature_files) == 1:
    ok(f"1 fichier .feature généré")
else:
    fail(f"Attendu 1 fichier .feature | Reçu : {len(feature_files)}")

# 4.5 - Nettoyage du dossier de test
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
    ok(f"Dossier de test nettoyé : {OUTPUT_DIR}")


# ══════════════════════════════════════════════════════════
# TEST 5 : Configuration .env - Clé API
# ══════════════════════════════════════════════════════════
section("TEST 5 : Configuration .env - Clé API OpenAI")

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
api_key = os.getenv("OPENAI_API_KEY", "")

if not api_key or api_key == "your_openai_api_key_here":
    warn("OPENAI_API_KEY non configurée → éditez le fichier .env")
elif not api_key.startswith("sk-"):
    warn(f"OPENAI_API_KEY format inhabituel : '{api_key[:8]}...'")
else:
    ok("OPENAI_API_KEY configurée et valide (commence par 'sk-')")

model = os.getenv("MODEL", "gpt-4o")
ok(f"Modèle configuré : {model}")

output_dir = os.getenv("OUTPUT_DIR", "./output")
ok(f"OUTPUT_DIR configuré : {output_dir}")


# ══════════════════════════════════════════════════════════
# RÉSUMÉ FINAL
# ══════════════════════════════════════════════════════════
total = passed + failed
print(f"\n{'═'*55}")
print(f"{BOLD}  RÉSULTATS FINAUX{RESET}")
print(f"{'═'*55}")
print(f"  {GREEN}✅ Passés  : {passed}{RESET}")
print(f"  {RED}❌ Échoués : {failed}{RESET}")
print(f"  {YELLOW}⚠️  Warnings: {warned}{RESET}")
print(f"  📊 Total   : {total}")
print(f"{'═'*55}\n")

if failed == 0:
    print(f"{GREEN}{BOLD}  🎉 Tous les tests sont passés !{RESET}\n")
else:
    print(f"{RED}{BOLD}  💥 {failed} test(s) échoué(s) - vérifiez les erreurs ci-dessus{RESET}\n")
    sys.exit(1)
