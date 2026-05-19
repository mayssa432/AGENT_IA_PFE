from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
import re
import json
import traceback
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ── Historique SQLite (Livrable #6) ──────────────────────────────────────
try:
    from history.db import (
        log_event, get_history, get_stats, clear_history,
        EVENT_ANALYSIS, EVENT_SELECTOR, EVENT_SCENARIO, EVENT_MOCK_SYNC, EVENT_PIPELINE,
    )
    _HAS_HISTORY = True
except Exception:
    _HAS_HISTORY = False
    def log_event(*a, **kw): pass
    def get_history(*a, **kw): return []
    def get_stats(*a, **kw): return {}
    def clear_history(*a, **kw): return 0

# ── Métriques de performance (Livrable #8) ───────────────────────────────
try:
    from metrics.tracker import (
        track, get_runs, get_kpis, clear_metrics,
        OP_ANALYSIS, OP_SELECTOR, OP_SCENARIO, OP_MOCK_SYNC, OP_PIPELINE,
        STATUS_SUCCESS, STATUS_ERROR,
    )
    _HAS_METRICS = True
except Exception:
    _HAS_METRICS = False
    def track(*a, **kw): pass
    def get_runs(*a, **kw): return []
    def get_kpis(*a, **kw): return {}
    def clear_metrics(*a, **kw): return 0
    OP_ANALYSIS = OP_SELECTOR = OP_SCENARIO = OP_MOCK_SYNC = OP_PIPELINE = ""
    STATUS_SUCCESS = "success"; STATUS_ERROR = "error"

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

conversation_history = []
last_analysis_result = None
last_project_path = None

# Fichier de sauvegarde de l'analyse
ANALYSIS_CACHE_FILE = "last_analysis.json"


# ============================================================
#   SAUVEGARDE / CHARGEMENT DE L'ANALYSE
# ============================================================

def save_analysis(result, project_path):
    """Sauvegarde le resultat d'analyse dans un fichier JSON"""
    try:
        with open(ANALYSIS_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                "result": result,
                "project_path": project_path
            }, f, ensure_ascii=False, indent=2)
        print(f"[INFO] Analyse sauvegardee dans {ANALYSIS_CACHE_FILE}")
    except Exception as e:
        print(f"[WARN] Impossible de sauvegarder l'analyse : {e}")


def load_analysis():
    """Charge le dernier resultat d'analyse depuis le fichier JSON"""
    global last_analysis_result, last_project_path
    if os.path.exists(ANALYSIS_CACHE_FILE):
        try:
            with open(ANALYSIS_CACHE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                last_analysis_result = data.get("result")
                last_project_path = data.get("project_path")
                nb_issues = len(last_analysis_result.get('issues', []))
                print(f"[INFO] Analyse rechargee depuis {ANALYSIS_CACHE_FILE}")
                print(f"[INFO] Projet : {last_project_path}")
                print(f"[INFO] Issues : {nb_issues}")
        except Exception as e:
            print(f"[WARN] Impossible de charger l'analyse : {e}")


# Charger l'analyse au demarrage
load_analysis()


# ============================================================
#   ROUTES FLASK
# ============================================================

@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    global last_analysis_result, last_project_path
    data = request.json
    user_message = data.get("message", "")
    project_path = data.get("path", "")

    if project_path:
        last_project_path = project_path

    conversation_history.append({"role": "user", "content": user_message})
    response = handle_message(user_message, project_path)
    conversation_history.append({"role": "assistant", "content": response})

    return jsonify({"response": response})


@app.route("/analyze", methods=["POST"])
def analyze():
    global last_analysis_result, last_project_path
    data = request.json
    path = data.get("path", "").strip()

    if not path or not os.path.exists(path):
        return jsonify({"error": f"Chemin introuvable : {path}"}), 400

    last_project_path = path

    _t0_analyze = time.perf_counter()
    try:
        from agent import AppiumAgent
        agent = AppiumAgent()
        report = agent.analyze(path)

        result = {
            "files_analyzed": report.total_files,
            "total_issues": report.total_issues,
            "critical": report.critical_count,
            "important": report.important_count,
            "warning": report.warning_count,
            "summary": report.summary,
            "files_with_issues": [
                {
                    "name": f.file_name,
                    "issues_count": len(f.issues)
                }
                for f in report.files if f.issues
            ],
            "issues": [
                {
                    "file": f.file_name,
                    "severity": i.severity.value,
                    "detail": i.detail,
                    "line": i.line if i.line else "?"
                }
                for f in report.files
                for i in f.issues
            ]
        }

        last_analysis_result = result

        # Sauvegarder l'analyse pour persistence
        save_analysis(result, path)

        # Historique SQLite
        log_event(EVENT_ANALYSIS, {
            "files":    result["files_analyzed"],
            "issues":   result["total_issues"],
            "critical": result["critical"],
            "path":     path,
        })
        # Métriques perf
        track(OP_ANALYSIS, int((time.perf_counter()-_t0_analyze)*1000), STATUS_SUCCESS,
              files=result["files_analyzed"], issues=result["total_issues"])
        return jsonify(result)

    except Exception as e:
        log_event(EVENT_ANALYSIS, {"path": path, "error": str(e)}, status="error")
        track(OP_ANALYSIS, int((time.perf_counter()-_t0_analyze)*1000), STATUS_ERROR)
        return jsonify({"error": str(e)}), 500


@app.route("/dom/inspect", methods=["POST"])
def dom_inspect():
    data = request.json
    if not data:
        return jsonify({"error": "Payload JSON requis"}), 400

    capabilities = data.get("capabilities")
    if not capabilities or not isinstance(capabilities, dict):
        return jsonify({"error": "Le champ 'capabilities' est requis et doit être un objet JSON."}), 400

    java_file = data.get("java_file")
    validate = data.get("validate", False)
    fix = data.get("fix", False)
    snapshot_name = data.get("snapshot_name")
    report_name = data.get("report_name")
    output_dir = data.get("output_dir", "dom_snapshots")
    report_dir = data.get("report_dir", "dom_reports")
    server_url = data.get("server_url", os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723"))

    from dom_inspector.dom_inspector import DomInspector

    inspector = DomInspector(appium_server_url=server_url, output_dir=output_dir)

    try:
        snapshot = inspector.capture_dom(capabilities, snapshot_name=snapshot_name)
    except Exception as e:
        return jsonify({"error": f"Erreur capture DOM : {str(e)}"}), 500

    root = inspector.parse_snapshot(snapshot.xml)
    response = {
        "snapshot": {
            "path": snapshot.path,
            "metadata": snapshot.metadata,
        },
        "elements_count": len(root.xpath('//*')),
    }

    if validate:
        if not java_file:
            return jsonify({"error": "Le champ 'java_file' est requis pour la validation."}), 400
        if not os.path.exists(java_file):
            return jsonify({"error": f"Fichier Java introuvable : {java_file}"}), 400

        validation_issues = inspector.validate_page_object(java_file, root)
        response["validation"] = {
            "file": java_file,
            "issues_count": len(validation_issues),
            "issues": validation_issues,
        }

    if fix:
        if not java_file:
            return jsonify({"error": "Le champ 'java_file' est requis pour la correction."}), 400
        if not os.path.exists(java_file):
            return jsonify({"error": f"Fichier Java introuvable : {java_file}"}), 400

        fix_result = inspector.fix_page_object(java_file, root)
        response["fix"] = fix_result

    if validate or fix:
        try:
            report = inspector.generate_validation_report(java_file, root)
            inspector.report_manager.output_dir = report_dir
            report_path = inspector.save_validation_report(report, report_name)
            response["report"] = {
                "path": report_path,
                "generated": True,
            }
        except Exception as e:
            response["report_error"] = str(e)

    return jsonify(response)


@app.route("/dom/snapshots", methods=["GET"])
def dom_snapshots():
    from dom_inspector.dom_inspector import DomInspector

    inspector = DomInspector()
    snapshots = inspector.snapshot_manager.list_snapshots()
    return jsonify({"snapshots": snapshots})


@app.route("/dom/snapshot/<name>", methods=["GET"])
def dom_snapshot(name):
    from dom_inspector.dom_inspector import DomInspector

    inspector = DomInspector()
    try:
        snapshot = inspector.load_snapshot(name)
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

    return jsonify({
        "path": snapshot.path,
        "created_at": snapshot.created_at.isoformat() + "Z",
        "metadata": snapshot.metadata,
    })


@app.route("/validate", methods=["POST"])
def validate_page_object():
    """Valide un fichier Page Object uploade contre un snapshot DOM"""
    if 'java_file' not in request.files:
        return jsonify({"error": "Fichier Java requis"}), 400

    file = request.files['java_file']
    snapshot_name = request.form.get('snapshot_name')

    if not file.filename or not snapshot_name:
        return jsonify({"error": "Nom de fichier et snapshot requis"}), 400

    # Sauvegarder temporairement le fichier uploade
    import tempfile
    import os
    with tempfile.NamedTemporaryFile(mode='w', suffix='.java', delete=False) as temp_file:
        temp_file.write(file.read().decode('utf-8'))
        temp_java_path = temp_file.name

    try:
        from dom_inspector.dom_inspector import DomInspector
        inspector = DomInspector()

        # Charger le snapshot
        snapshot = inspector.load_snapshot(snapshot_name)
        root = inspector.parse_snapshot(snapshot.xml)

        # Valider
        validation_issues = inspector.validate_page_object(temp_java_path, root)

        # Generer le rapport
        report = inspector.generate_validation_report(temp_java_path, root)
        report_path = inspector.save_validation_report(report)

        return jsonify({
            "file": file.filename,
            "snapshot": snapshot_name,
            "issues_count": len(validation_issues),
            "issues": validation_issues,
            "report_path": report_path,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Nettoyer le fichier temporaire
        if os.path.exists(temp_java_path):
            os.unlink(temp_java_path)


@app.route("/fix", methods=["POST"])
def fix_page_object():
    """Corrige automatiquement un fichier Page Object uploade"""
    if 'java_file' not in request.files:
        return jsonify({"error": "Fichier Java requis"}), 400

    file = request.files['java_file']
    snapshot_name = request.form.get('snapshot_name')

    if not file.filename or not snapshot_name:
        return jsonify({"error": "Nom de fichier et snapshot requis"}), 400

    # Sauvegarder temporairement le fichier uploade
    import tempfile
    import os
    with tempfile.NamedTemporaryFile(mode='w', suffix='.java', delete=False) as temp_file:
        temp_file.write(file.read().decode('utf-8'))
        temp_java_path = temp_file.name

    try:
        from dom_inspector.dom_inspector import DomInspector
        inspector = DomInspector()

        # Charger le snapshot
        snapshot = inspector.load_snapshot(snapshot_name)
        root = inspector.parse_snapshot(snapshot.xml)

        # Corriger
        fix_result = inspector.fix_page_object(temp_java_path, root)

        # Generer le rapport
        report = inspector.generate_validation_report(temp_java_path, root)
        report_path = inspector.save_validation_report(report)

        return jsonify({
            "file": file.filename,
            "snapshot": snapshot_name,
            "fix_result": fix_result,
            "report_path": report_path,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Nettoyer le fichier temporaire
        if os.path.exists(temp_java_path):
            os.unlink(temp_java_path)


# ============================================================
#   FONCTIONS UTILITAIRES
# ============================================================

def extraire_nom_fichier(message):
    """Extrait le nom d'un fichier Java mentionne dans le message"""
    patterns = [
        r'(\w+po)',
        r'(\w+page)',
        r'(\w+screen)',
        r'(\w+\.java)',
    ]
    for pattern in patterns:
        match = re.search(pattern, message.lower())
        if match:
            nom = match.group(1).replace('.java', '')
            return nom
    return None


def format_issues_par_fichier(result, fichier, severity=None):
    """Affiche les problemes d'un fichier specifique"""
    issues = result.get("issues", [])

    issues_fichier = [
        i for i in issues
        if fichier.lower() in i.get("file", "").lower()
    ]

    if severity:
        issues_fichier = [
            i for i in issues_fichier
            if i.get("severity") == severity
        ]

    if not issues_fichier:
        label = 'critique ' if severity == 'CRITICAL' else ''
        return (
            f"Aucun probleme {label}trouve "
            f"dans les fichiers contenant **{fichier}** !"
        )

    nom_fichier = issues_fichier[0].get("file", fichier)

    severity_label = {
        "CRITICAL": "critique(s)",
        "IMPORTANT": "important(s)",
        None: "au total"
    }.get(severity, "")

    response = (
        f"**{nom_fichier}** — "
        f"{len(issues_fichier)} probleme(s) {severity_label} :\n\n"
    )

    for i in issues_fichier:
        sev_icon = "CRITIQUE" if i.get("severity") == "CRITICAL" else "IMPORTANT"
        response += (
            f"[{sev_icon}] **Ligne {i.get('line')}** : "
            f"{i.get('detail')}\n\n"
        )

    response += f"\nTapez **corrige {nom_fichier}** pour les suggestions."
    response += (
        f"\nTapez **applique correction {nom_fichier}** "
        f"pour corriger automatiquement."
    )
    return response


def format_corrections_par_fichier(result, fichier):
    """Affiche les corrections pour un fichier specifique"""
    issues = result.get("issues", [])

    issues_fichier = [
        i for i in issues
        if fichier.lower() in i.get("file", "").lower()
        and i.get("severity") == "CRITICAL"
    ]

    if not issues_fichier:
        return (
            f"Aucun probleme critique a corriger "
            f"dans les fichiers contenant **{fichier}** !"
        )

    nom_fichier = issues_fichier[0].get("file", fichier)
    response = (
        f"**Corrections pour `{nom_fichier}`** — "
        f"{len(issues_fichier)} probleme(s) :\n\n"
    )

    for i in issues_fichier:
        line = i.get('line', '?')
        detail = i.get('detail', '?')
        response += f"**Ligne {line}** : {detail}\n"

        if "crochets non equilibres" in detail or "crochets" in detail:
            response += "Correction : Verifiez que chaque `[` a son `]`.\n"
            response += "Exemple : `//android.widget.TextView[@text='valeur']`\n\n"
        elif "parentheses non equilibrees" in detail or "parentheses" in detail:
            response += "Correction : Verifiez que chaque `(` a son `)`.\n"
            response += "Exemple : `(//XCUIElementTypeOther[@name='valeur'])[1]`\n\n"
        elif "doublon" in detail.lower():
            response += "Correction : Supprimez le champ duplique ou renommez-le.\n\n"
        elif "annotation" in detail.lower():
            response += "Correction : Ajoutez `@AndroidFindBy` ou `@iOSXCUITFindBy`.\n\n"
        else:
            response += "Correction : Verifiez la syntaxe du selecteur.\n\n"

    response += (
        f"\nTapez **applique correction {nom_fichier}** "
        f"pour corriger automatiquement le fichier."
    )
    return response


# ============================================================
#   CORRECTION AUTOMATIQUE — FICHIER SPECIFIQUE
# ============================================================

def appliquer_correction_fichier(fichier, project_path):
    """Applique la correction automatique sur un fichier specifique"""
    global last_analysis_result

    if not last_analysis_result:
        return "Aucune analyse effectuee. Lancez une analyse d'abord."

    if not project_path or not os.path.exists(project_path):
        return "Chemin du projet invalide. Verifiez le chemin dans la barre a gauche."

    try:
        from xpath_fixer import XPathFixer
        fixer = XPathFixer()

        all_issues = last_analysis_result.get("issues", [])

        # Debug
        print(f"[DEBUG] Fichier cherche : {fichier}")
        fichiers_issues = list(set(i.get('file', '') for i in all_issues))
        print(f"[DEBUG] Fichiers dans issues : {fichiers_issues}")

        # Chercher le fichier dans le projet
        file_path = fixer.find_file(project_path, fichier + ".java")
        if not file_path:
            file_path = fixer.find_file(project_path, fichier)

        print(f"[DEBUG] Fichier trouve : {file_path}")

        if not file_path:
            fichiers_java = []
            for root, dirs, files in os.walk(project_path):
                for f in files:
                    if f.endswith('.java'):
                        fichiers_java.append(f)
            liste = "\n".join([
                f"- `{f}`" for f in sorted(fichiers_java)[:15]
            ])
            return (
                f"Fichier `{fichier}.java` introuvable.\n\n"
                f"Fichiers Java disponibles :\n{liste}"
            )

        # Nom reel du fichier avec la bonne casse
        real_name = os.path.basename(file_path)
        print(f"[DEBUG] Nom reel : {real_name}")

        # Filtrer les issues avec correspondance exacte insensible a la casse
        issues_critiques = [
            i for i in all_issues
            if i.get("file", "").lower() == real_name.lower()
            and i.get("severity") == "CRITICAL"
        ]

        print(f"[DEBUG] Issues critiques : {len(issues_critiques)}")

        if not issues_critiques:
            toutes_issues = [
                i for i in all_issues
                if i.get("file", "").lower() == real_name.lower()
            ]
            print(f"[DEBUG] Toutes issues du fichier : {toutes_issues}")

            if toutes_issues:
                detail = "\n".join([
                    f"- Ligne {i.get('line')} "
                    f"[{i.get('severity')}] : {i.get('detail')}"
                    for i in toutes_issues
                ])
                return (
                    f"Aucun probleme CRITIQUE dans `{real_name}`.\n\n"
                    f"Problemes trouves ({len(toutes_issues)}) :\n{detail}"
                )
            else:
                return (
                    f"Aucun probleme trouve pour `{real_name}`.\n\n"
                    f"Tapez **critiques** pour voir tous les problemes."
                )

        # Appliquer les corrections
        result = fixer.fix_file(file_path, issues_critiques)
        return fixer.format_correction_report(result)

    except Exception as e:
        return f"Erreur : {str(e)}\n{traceback.format_exc()}"


# ============================================================
#   CORRECTION AUTOMATIQUE — TOUS LES FICHIERS
# ============================================================

def appliquer_toutes_corrections(project_path):
    """Applique les corrections sur tous les fichiers"""
    global last_analysis_result

    if not last_analysis_result:
        return "Aucune analyse effectuee. Lancez une analyse d'abord."

    if not project_path or not os.path.exists(project_path):
        return "Chemin du projet invalide."

    try:
        from xpath_fixer import XPathFixer
        fixer = XPathFixer()

        result = fixer.fix_all_files(project_path, last_analysis_result)

        total_files = result.get("total_files_fixed", 0)
        total_corrections = result.get("total_corrections", 0)
        results = result.get("results", [])

        response = "**Correction automatique terminee !**\n\n"
        response += f"Fichiers corriges : **{total_files}**\n"
        response += f"Corrections appliquees : **{total_corrections}**\n\n"
        response += "**Detail par fichier :**\n\n"

        for r in results:
            if r.get("success"):
                response += (
                    f"OK `{r.get('file')}` — "
                    f"{r.get('corrections_count')} correction(s)\n"
                )
            else:
                response += f"ERREUR `{r.get('file')}` — {r.get('error')}\n"

        response += "\nSauvegardes creees dans le dossier `backups/`"
        response += "\nTapez **analyser** pour verifier les corrections."

        return response

    except Exception as e:
        return f"Erreur : {str(e)}\n{traceback.format_exc()}"


# ============================================================
#   GESTION DES MESSAGES
# ============================================================

def handle_message(message, path):
    global last_analysis_result, last_project_path
    message_lower = message.lower()

    project_path = (
        path if path and os.path.exists(path)
        else last_project_path
    )

    # Salutation / Aide
    if any(word in message_lower for word in [
        "bonjour", "hello", "salut", "aide", "help"
    ]):
        return (
            "Bonjour ! Je suis votre Agent IA Appium.\n\n"
            "Commandes disponibles :\n"
            "- **analyser** : lancer une analyse\n"
            "- **resume** : voir les resultats\n"
            "- **critique(s)** : voir les problemes urgents\n"
            "- **importants** : voir les problemes importants\n"
            "- **corriger** : suggestions de correction\n"
            "- **applique correction ConsentPO** : corriger un fichier\n"
            "- **applique tout** : corriger tous les fichiers\n"
            "- **generer** : rapport complet\n"
            "- **fichiers** : liste des fichiers\n"
            "- **capture dom** : instructions pour lancer DOM Inspector via API\n"
            "- **valide java** : instructions pour vérifier un Page Object Java\n"
            "- **corrige java** : instructions pour corriger un Page Object Java\n"
            "- **upload valide** : valider un fichier Page Object via upload web\n"
            "- **upload corrige** : corriger un fichier Page Object via upload web\n"
            "- **NomFichier** : problemes d'un fichier specifique"
        )

    # Analyse
    elif any(word in message_lower for word in [
        "analyser", "analyse", "scanner", "scan"
    ]):
        if project_path and os.path.exists(project_path):
            try:
                from agent import AppiumAgent
                agent = AppiumAgent()
                report = agent.analyze(project_path)

                last_analysis_result = {
                    "files_analyzed": report.total_files,
                    "total_issues": report.total_issues,
                    "critical": report.critical_count,
                    "important": report.important_count,
                    "warning": report.warning_count,
                    "summary": report.summary,
                    "files_with_issues": [
                        {
                            "name": f.file_name,
                            "issues_count": len(f.issues)
                        }
                        for f in report.files if f.issues
                    ],
                    "issues": [
                        {
                            "file": f.file_name,
                            "severity": i.severity.value,
                            "detail": i.detail,
                            "line": i.line if i.line else "?"
                        }
                        for f in report.files
                        for i in f.issues
                    ]
                }

                # Sauvegarder pour persistence
                save_analysis(last_analysis_result, project_path)

                return format_analysis_result(last_analysis_result)

            except Exception as e:
                return f"Erreur lors de l'analyse : {str(e)}"
        else:
            return "Veuillez entrer un chemin de projet valide."

    # Resume
    elif any(word in message_lower for word in [
        "resume", "summary", "resultat"
    ]):
        if last_analysis_result:
            return format_analysis_result(last_analysis_result)
        else:
            return "Aucune analyse effectuee. Cliquez sur Analyser d'abord."

    # Problemes critiques
    elif any(word in message_lower for word in [
        "critique", "critical", "urgent"
    ]):
        if last_analysis_result:
            fichier = extraire_nom_fichier(message_lower)
            if fichier:
                return format_issues_par_fichier(
                    last_analysis_result, fichier, "CRITICAL"
                )
            return format_critical_issues(last_analysis_result)
        else:
            return "Aucune analyse effectuee. Cliquez sur Analyser d'abord."

    # Problemes importants
    elif any(word in message_lower for word in [
        "important", "importants"
    ]):
        if last_analysis_result:
            fichier = extraire_nom_fichier(message_lower)
            if fichier:
                return format_issues_par_fichier(
                    last_analysis_result, fichier, "IMPORTANT"
                )
            return format_important_issues(last_analysis_result)
        else:
            return "Aucune analyse effectuee. Cliquez sur Analyser d'abord."

    # Correction automatique — Tous les fichiers
    elif any(word in message_lower for word in [
        "applique tout", "corriger tout", "fix all", "tout corriger"
    ]):
        if last_analysis_result:
            return appliquer_toutes_corrections(project_path)
        else:
            return "Aucune analyse effectuee. Cliquez sur Analyser d'abord."

    # Correction automatique — Fichier specifique
    elif any(word in message_lower for word in [
        "applique correction", "applique", "automatique", "auto"
    ]):
        if last_analysis_result:
            fichier = extraire_nom_fichier(message_lower)
            if fichier:
                return appliquer_correction_fichier(fichier, project_path)
            else:
                return "Precisez le fichier : **applique correction ConsentPO**"
        else:
            return "Aucune analyse effectuee. Cliquez sur Analyser d'abord."

    # Corrections — Suggestions
    elif any(word in message_lower for word in [
        "corriger", "correction", "fix", "reparer", "corrige"
    ]):
        if last_analysis_result:
            fichier = extraire_nom_fichier(message_lower)
            if fichier:
                return format_corrections_par_fichier(
                    last_analysis_result, fichier
                )
            return format_corrections(last_analysis_result)
        else:
            return "Aucune analyse effectuee. Cliquez sur Analyser d'abord."

    # Rapport complet
    elif any(word in message_lower for word in [
        "generer", "rapport", "report", "exporter"
    ]):
        if last_analysis_result:
            return format_full_report(last_analysis_result)
        else:
            return "Aucune analyse effectuee. Cliquez sur Analyser d'abord."

    # Liste des fichiers
    elif any(word in message_lower for word in [
        "fichier", "file", "liste"
    ]):
        if last_analysis_result:
            return format_files_list(last_analysis_result)
        else:
            return "Aucune analyse effectuee. Cliquez sur Analyser d'abord."

    # Detection automatique d'un nom de fichier
    elif last_analysis_result:
        fichier = extraire_nom_fichier(message_lower)
        if fichier:
            return format_issues_par_fichier(last_analysis_result, fichier)
        return (
            "Je n'ai pas compris votre demande.\n\n"
            "Tapez **aide** pour voir les commandes disponibles."
        )

    else:
        return (
            "Je n'ai pas compris votre demande.\n\n"
            "Tapez **aide** pour voir les commandes disponibles."
        )


# ============================================================
#   FONCTIONS DE FORMATAGE
# ============================================================

def format_analysis_result(result):
    if not result:
        return "Aucun resultat disponible."

    files = result.get("files_analyzed", 0)
    total = result.get("total_issues", 0)
    critical = result.get("critical", 0)
    important = result.get("important", 0)
    clean = files - len(result.get("files_with_issues", []))

    return (
        f"**Analyse terminee !**\n\n"
        f"Fichiers analyses : **{files}**\n"
        f"Fichiers propres : **{clean}**\n"
        f"Problemes detectes : **{total}**\n"
        f"Critiques : **{critical}**\n"
        f"Importants : **{important}**\n\n"
        f"Tapez **critiques** pour voir les problemes urgents.\n"
        f"Tapez **importants** pour voir les problemes importants.\n"
        f"Tapez **corriger** pour les suggestions de correction.\n"
        f"Tapez **applique tout** pour corriger automatiquement.\n"
        f"Tapez **fichiers** pour voir la liste complete.\n"
        f"Tapez le **nom d'un fichier** (ex: ConsentPO) pour ses problemes."
    )


def format_critical_issues(result):
    issues = result.get("issues", [])
    critical = [i for i in issues if i.get("severity") == "CRITICAL"]

    if not critical:
        return "Aucun probleme critique detecte !"

    response = f"**{len(critical)} probleme(s) critique(s) :**\n\n"
    for i in critical[:10]:
        response += (
            f"`{i.get('file')}` — "
            f"Ligne {i.get('line')} : {i.get('detail')}\n\n"
        )

    if len(critical) > 10:
        response += f"... et **{len(critical) - 10}** autres problemes critiques.\n"
        response += "Tapez le **nom d'un fichier** pour ses problemes specifiques."

    return response


def format_important_issues(result):
    issues = result.get("issues", [])
    important = [i for i in issues if i.get("severity") == "IMPORTANT"]

    if not important:
        return "Aucun probleme important detecte !"

    response = f"**{len(important)} probleme(s) important(s) :**\n\n"
    for i in important[:10]:
        response += (
            f"`{i.get('file')}` — "
            f"Ligne {i.get('line')} : {i.get('detail')}\n\n"
        )

    if len(important) > 10:
        response += f"... et **{len(important) - 10}** autres problemes importants.\n"
        response += "Tapez le **nom d'un fichier** pour ses problemes specifiques."

    return response


def format_corrections(result):
    issues = result.get("issues", [])
    critical = [i for i in issues if i.get("severity") == "CRITICAL"]

    if not critical:
        return "Aucun probleme a corriger !"

    response = (
        f"**Suggestions de correction pour "
        f"{len(critical)} probleme(s) critique(s) :**\n\n"
    )

    for i in critical[:5]:
        file = i.get('file', '?')
        line = i.get('line', '?')
        detail = i.get('detail', '?')

        response += f"**`{file}`** — Ligne {line}\n"
        response += f"Probleme : {detail}\n"

        if "crochets" in detail:
            response += "Correction : Verifiez que chaque `[` a son `]`.\n"
            response += "Exemple : `//android.widget.TextView[@text='valeur']`\n\n"
        elif "parentheses" in detail:
            response += "Correction : Verifiez que chaque `(` a son `)`.\n"
            response += "Exemple : `(//XCUIElementTypeOther[@name='valeur'])[1]`\n\n"
        elif "doublon" in detail.lower():
            response += "Correction : Supprimez le champ duplique ou renommez-le.\n\n"
        elif "annotation" in detail.lower():
            response += "Correction : Ajoutez `@AndroidFindBy` ou `@iOSXCUITFindBy`.\n\n"
        else:
            response += "Correction : Verifiez la syntaxe du selecteur.\n\n"

    if len(critical) > 5:
        response += f"... et **{len(critical) - 5}** autres problemes.\n"
        response += "Tapez **corrige NomFichier** pour un fichier specifique.\n"
        response += "Tapez **applique tout** pour corriger automatiquement."

    return response


def format_full_report(result):
    files = result.get("files_analyzed", 0)
    total = result.get("total_issues", 0)
    critical = result.get("critical", 0)
    important = result.get("important", 0)
    warning = result.get("warning", 0)
    files_with_issues = result.get("files_with_issues", [])
    clean = files - len(files_with_issues)

    response = (
        f"**RAPPORT COMPLET D'ANALYSE**\n"
        f"{'=' * 40}\n\n"
        f"**Statistiques generales :**\n"
        f"- Fichiers analyses : **{files}**\n"
        f"- Fichiers propres : **{clean}**\n"
        f"- Fichiers avec problemes : **{len(files_with_issues)}**\n\n"
        f"**Problemes detectes : {total}**\n"
        f"- Critiques : **{critical}**\n"
        f"- Importants : **{important}**\n"
        f"- Avertissements : **{warning}**\n\n"
        f"**Fichiers concernes :**\n"
    )

    for f in files_with_issues:
        response += (
            f"  - `{f.get('name')}` — "
            f"{f.get('issues_count')} probleme(s)\n"
        )

    response += (
        "\n**Prochaines etapes :**\n"
        "- Tapez **corriger** pour les suggestions\n"
        "- Tapez **applique tout** pour corriger automatiquement\n"
        "- Tapez **critiques** pour les problemes urgents\n"
        "- Tapez le **nom d'un fichier** pour ses problemes"
    )

    return response


def format_files_list(result):
    files = result.get("files_with_issues", [])
    if not files:
        return "Tous les fichiers sont propres !"

    response = f"**Fichiers avec problemes ({len(files)}) :**\n\n"
    for f in files:
        response += (
            f"- `{f.get('name')}` — "
            f"{f.get('issues_count')} probleme(s)\n"
        )

    response += "\nTapez le **nom d'un fichier** pour ses problemes detailles."
    response += "\nTapez **applique tout** pour corriger automatiquement."
    return response


# ============================================================
#   NOUVELLES ROUTES — LIVRABLE #5 (dashboard unifié)
# ============================================================

@app.route("/selector-fix", methods=["POST"])
def selector_fix_api():
    """Livrable #2 : détection + correction automatique des sélecteurs cassés."""
    _t0_sf = time.perf_counter()
    data = request.json or {}
    po_file = data.get("po_file", "").strip()

    if not po_file or not os.path.exists(po_file):
        # Chercher un fichier .java depuis le projet connu
        if last_project_path and os.path.exists(last_project_path):
            import glob
            java_files = glob.glob(os.path.join(last_project_path, "**", "*.java"), recursive=True)
            if java_files:
                po_file = java_files[0]
            else:
                return jsonify({"error": "Aucun fichier Java trouvé dans le projet."}), 400
        else:
            return jsonify({"error": f"Fichier Java introuvable : {po_file}"}), 400

    try:
        from dom_inspector.ui_parser import UiParser
        from dom_inspector.selector_validator import SelectorValidator
        from dom_inspector.selector_fixer import SelectorFixer

        # Chercher un snapshot DOM disponible
        snapshots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dom_snapshots")
        xml_files = []
        if os.path.exists(snapshots_dir):
            import glob
            xml_files = glob.glob(os.path.join(snapshots_dir, "**", "*.xml"), recursive=True)

        # DOM minimal si aucun snapshot réel disponible
        INLINE_DOM = """<?xml version="1.0" encoding="UTF-8"?>
<hierarchy rotation="0">
  <android.widget.FrameLayout resource-id="com.orange.otvp:id/root_view" bounds="[0,0][1080,1920]">
    <android.widget.LinearLayout resource-id="com.orange.otvp:id/main_container">
      <android.widget.TextView resource-id="com.orange.otvp:id/live_channel_title" text="Orange TV" bounds="[0,100][500,150]"/>
      <android.widget.Button resource-id="com.orange.otvp:id/btn_play" text="Lecture" bounds="[0,200][300,250]"/>
      <android.widget.ImageView resource-id="com.orange.otvp:id/channel_logo" bounds="[0,300][100,400]"/>
      <android.widget.TextView resource-id="com.orange.otvp:id/program_title" text="Journal de 20h" bounds="[0,400][500,450]"/>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>"""

        if xml_files:
            dom_path = xml_files[0]
            with open(dom_path, "r", encoding="utf-8") as f:
                dom_xml = f.read()
        else:
            dom_xml = INLINE_DOM
            dom_path = "dom-demo-inline"

        parser = UiParser()
        dom_root = parser.parse_xml(dom_xml)

        validator = SelectorValidator()
        issues = validator.validate_file(po_file, dom_root)

        # Correction automatique (dry-run : lit mais n'écrit pas)
        fixer = SelectorFixer()
        fix_result = fixer.fix_file(po_file, dom_root)
        corrections = fix_result.get("corrections", [])
        fixed_count = len(corrections)

        result_sf = {
            "po_file": os.path.basename(po_file),
            "dom_source": os.path.basename(dom_path),
            "broken_count": len(issues),
            "fixed_count": fixed_count,
            "issues": [
                {
                    "field": i.get("selector_name", "?"),
                    "selector": i.get("selector_value", "?"),
                    "reason": i.get("message", "Sélecteur invalide"),
                }
                for i in issues[:20]
            ],
            "fixes": [
                {
                    "field": c.get("suggestion", {}).get("param_name", "?"),
                    "old": c.get("original", "?"),
                    "new": c.get("fixed", "?"),
                    "confidence": c.get("suggestion", {}).get("confidence", "medium"),
                }
                for c in corrections[:20]
            ],
        }
        log_event(EVENT_SELECTOR, {
            "po_file": result_sf["po_file"],
            "broken":  result_sf["broken_count"],
            "fixed":   result_sf["fixed_count"],
        }, status="ok" if result_sf["broken_count"] == 0 else "partial")
        track(OP_SELECTOR, int((time.perf_counter()-_t0_sf)*1000), STATUS_SUCCESS,
              broken=result_sf["broken_count"], fixed=result_sf["fixed_count"])
        return jsonify(result_sf)

    except Exception as e:
        log_event(EVENT_SELECTOR, {"po_file": os.path.basename(po_file), "error": str(e)}, status="error")
        track(OP_SELECTOR, int((time.perf_counter()-_t0_sf)*1000), STATUS_ERROR)
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500


@app.route("/scenario-generate", methods=["POST"])
def scenario_generate_api():
    """Livrable #4 : génération automatique de scénarios BDD depuis un Page Object."""
    _t0_sg = time.perf_counter()
    data = request.json or {}
    po_file = data.get("po_file", "").strip()
    mode = data.get("mode", "offline")  # "llm" ou "offline"

    # Chemin par défaut : AuthenticationPO.java
    pages_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "AGENT_IA_PFE", "src", "test", "java",
        "com", "orange", "otvp", "automation", "pages", "mobile"
    )

    if not po_file or not os.path.exists(po_file):
        default_po = os.path.join(pages_dir, "AuthenticationPO.java")
        if os.path.exists(default_po):
            po_file = default_po
        else:
            # Chercher n'importe quel .java
            import glob
            java_files = glob.glob(os.path.join(pages_dir, "*.java"))
            if java_files:
                po_file = java_files[0]
            else:
                return jsonify({"error": "Aucun fichier Java trouvé pour la génération."}), 400

    try:
        from demo_scenario_generator import run_pipeline
        from pathlib import Path
        import io
        from contextlib import redirect_stdout, redirect_stderr
        captured = io.StringIO()
        with redirect_stdout(captured), redirect_stderr(captured):
            report = run_pipeline(Path(po_file), offline=(mode == "offline"))

        feature_v = report.get("steps", {}).get("step2_feature", {}).get("validation", {})
        steps_v   = report.get("steps", {}).get("step3_step_definitions", {}).get("validation", {})

        result_sg = {
            "po_file":        os.path.basename(po_file),
            "mode":           mode,
            "success":        report.get("success", False),
            "scenario_count": feature_v.get("scenario_count", 0),
            "step_count":     steps_v.get("step_count", 0),
            "feature_source": report.get("steps", {}).get("step2_feature", {}).get("source", "?"),
            "files": {
                "feature": report.get("files", {}).get("feature", ""),
                "steps":   report.get("files", {}).get("steps", ""),
                "runner":  report.get("files", {}).get("runner", ""),
            },
        }
        log_event(EVENT_SCENARIO, {
            "po_file":       result_sg["po_file"],
            "scenario_count": result_sg["scenario_count"],
            "step_count":    result_sg["step_count"],
            "mode":          mode,
        }, status="ok" if result_sg["success"] else "partial")
        track(OP_SCENARIO, int((time.perf_counter()-_t0_sg)*1000), STATUS_SUCCESS,
              scenario_count=result_sg["scenario_count"], step_count=result_sg["step_count"])
        return jsonify(result_sg)

    except Exception as e:
        log_event(EVENT_SCENARIO, {"po_file": os.path.basename(po_file), "error": str(e)}, status="error")
        track(OP_SCENARIO, int((time.perf_counter()-_t0_sg)*1000), STATUS_ERROR)
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500


@app.route("/mock-sync", methods=["POST"])
def mock_sync_api():
    """Livrable #3 : comparaison sémantique réel vs mock + mise à jour automatique."""
    _t0_ms = time.perf_counter()
    try:
        from deepdiff import DeepDiff
        _has_deepdiff = True
    except ImportError:
        _has_deepdiff = False

    # Mock "version stockée"
    stored_mock = {
        "channels": [
            {"id": "ch1", "name": "TF1",      "logo": "tf1.png",    "position": 1},
            {"id": "ch2", "name": "France 2", "logo": "f2.png",     "position": 2},
            {"id": "ch3", "name": "M6",        "logo": "m6_old.png", "position": 3},
        ],
        "total": 3,
        "version": "1.0",
    }

    # "Réponse réelle" simulée (légèrement différente)
    real_response = {
        "channels": [
            {"id": "ch1", "name": "TF1",      "logo": "tf1.png",    "position": 1},
            {"id": "ch2", "name": "France 2", "logo": "f2_hd.png",  "position": 2},
            {"id": "ch3", "name": "M6",        "logo": "m6_new.png", "position": 3},
            {"id": "ch4", "name": "Canal+",    "logo": "cplus.png",  "position": 4},
        ],
        "total": 4,
        "version": "1.2",
    }

    diffs = []
    if _has_deepdiff:
        from deepdiff import DeepDiff
        raw = DeepDiff(stored_mock, real_response, ignore_order=True)
        for change_type, changes in raw.items():
            if isinstance(changes, dict):
                for path, detail in changes.items():
                    if hasattr(detail, 't1'):
                        diffs.append({"path": path, "old": str(detail.t1), "new": str(detail.t2), "type": "changed"})
                    else:
                        diffs.append({"path": path, "detail": str(detail), "type": change_type})
            elif isinstance(changes, set):
                for item in changes:
                    diffs.append({"path": str(item), "type": change_type})
    else:
        # Diff basique sans deepdiff
        if stored_mock.get("total") != real_response.get("total"):
            diffs.append({"path": "total", "old": str(stored_mock["total"]), "new": str(real_response["total"]), "type": "changed"})
        if stored_mock.get("version") != real_response.get("version"):
            diffs.append({"path": "version", "old": stored_mock["version"], "new": real_response["version"], "type": "changed"})
        s_logos = {c["id"]: c["logo"] for c in stored_mock["channels"]}
        r_logos = {c["id"]: c["logo"] for c in real_response["channels"]}
        for cid, logo in r_logos.items():
            if cid not in s_logos:
                diffs.append({"path": f"channels[{cid}]", "type": "added", "detail": f"new channel {cid}"})
            elif s_logos[cid] != logo:
                diffs.append({"path": f"channels[{cid}].logo", "old": s_logos[cid], "new": logo, "type": "changed"})

    # Sauvegarder le mock mis à jour
    from datetime import datetime, timezone
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "reports", "mock_versions")
    os.makedirs(out_dir, exist_ok=True)
    updated_path = os.path.join(out_dir, f"mock-live-api_{ts}.json")
    with open(updated_path, "w", encoding="utf-8") as f:
        json.dump(real_response, f, ensure_ascii=False, indent=2)

        resp_data = {
            "mock_id":       "mock-live-001",
            "endpoint":      "/api/v1/live/channels",
            "diffs_found":   len(diffs),
            "diffs":         diffs[:20],
            "mock_updated":  True,
            "backup_path":   os.path.relpath(updated_path),
            "deepdiff_used": _has_deepdiff,
        }
        log_event(EVENT_MOCK_SYNC, {
            "mock_id":    resp_data["mock_id"],
            "diffs_found": resp_data["diffs_found"],
            "mock_updated": resp_data["mock_updated"],
        }, status="ok" if resp_data["diffs_found"] == 0 else "partial")
        track(OP_MOCK_SYNC, int((time.perf_counter()-_t0_ms)*1000), STATUS_SUCCESS,
              diffs_found=resp_data["diffs_found"])
        return jsonify(resp_data)


@app.route("/pipeline", methods=["POST"])
def pipeline_api():
    """Lance le pipeline complet orchestrate.py (analyse + rapport)."""
    data = request.json or {}
    pages_path = data.get("pages_path", "").strip() or last_project_path or ""

    if not pages_path or not os.path.exists(pages_path):
        return jsonify({"error": f"Chemin introuvable : {pages_path}"}), 400

    try:
        import subprocess
        python_exe = sys.executable
        result = subprocess.run(
            [python_exe, "orchestrate.py", "--pages", pages_path, "--dry-run"],
            capture_output=True, text=True, timeout=120,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        return jsonify({
            "exit_code": result.returncode,
            "stdout":    result.stdout[-3000:] if result.stdout else "",
            "stderr":    result.stderr[-1000:] if result.stderr else "",
            "success":   result.returncode == 0,
        })
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Timeout : pipeline trop long (>120s)"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/status", methods=["GET"])
def status_api():
    """Retourne l'état global de l'agent (ping + stats dernière analyse)."""
    return jsonify({
        "status":        "online",
        "version":       "2.0",
        "last_analysis": {
            "files":    last_analysis_result.get("files_analyzed", 0) if last_analysis_result else 0,
            "issues":   last_analysis_result.get("total_issues", 0)   if last_analysis_result else 0,
            "critical": last_analysis_result.get("critical", 0)       if last_analysis_result else 0,
        } if last_analysis_result else None,
        "project_path": last_project_path,
    })


# ============================================================
#   ROUTES HISTORIQUE SQLITE — LIVRABLE #6
# ============================================================

@app.route("/history", methods=["GET"])
def history_list():
    """Retourne les derniers événements enregistrés."""
    event_type = request.args.get("type")
    status     = request.args.get("status")
    limit      = min(int(request.args.get("limit", 50)), 200)
    offset     = int(request.args.get("offset", 0))
    rows = get_history(event_type=event_type, status=status, limit=limit, offset=offset)
    return jsonify({"events": rows, "count": len(rows), "history_enabled": _HAS_HISTORY})


@app.route("/history/stats", methods=["GET"])
def history_stats():
    """Retourne les statistiques globales de l'historique."""
    stats = get_stats()
    stats["history_enabled"] = _HAS_HISTORY
    return jsonify(stats)


@app.route("/history/clear", methods=["POST"])
def history_clear():
    """Supprime l'historique (tous ou d'un type donné)."""
    event_type = (request.json or {}).get("event_type")
    deleted = clear_history(event_type=event_type)
    return jsonify({"deleted": deleted, "event_type": event_type or "all"})


# ============================================================
#   ROUTES APP MANAGER — LIVRABLE #9
# ============================================================

_MOCK_DEVICES = [
    {
        "serial": "emulator-5554", "model": "Nexus_5X", "brand": "Google",
        "android_version": "9.0", "api_level": "28", "resolution": "1080x1920",
        "state": "emulator",
    },
    {
        "serial": "FA7AB0305461", "model": "SM-G973F", "brand": "Samsung",
        "android_version": "11.0", "api_level": "30", "resolution": "1440x3040",
        "state": "device",
    },
]


def _adb_available():
    import subprocess
    try:
        subprocess.check_output(["adb", "version"], stderr=subprocess.STDOUT, timeout=3)
        return True
    except Exception:
        return False


@app.route("/devices", methods=["GET"])
def devices_list():
    """Livrable #9 : liste les devices Android (ADB réel ou mock)."""
    _t0_dev = time.perf_counter()
    mode = request.args.get("mode", "auto")  # "auto" | "mock" | "real"

    try:
        adb_ok = _adb_available() if mode != "mock" else False
        if adb_ok:
            from app_manager.device_manager import DeviceManager
            dm = DeviceManager()
            serials = dm.list_devices()
            devices = []
            for s in serials:
                try:
                    model   = dm.get_device_model(s) or "unknown"
                    version = dm.get_android_version(s) or "unknown"
                    devices.append({"serial": s, "model": model,
                                    "android_version": version, "state": "device"})
                except Exception:
                    devices.append({"serial": s, "model": "unknown",
                                    "android_version": "unknown", "state": "device"})
            src = "adb-real"
        else:
            devices = _MOCK_DEVICES
            src = "mock"

        track(OP_ANALYSIS, int((time.perf_counter()-_t0_dev)*1000), STATUS_SUCCESS,
              devices=len(devices))
        return jsonify({"devices": devices, "count": len(devices), "source": src})

    except Exception as e:
        track(OP_ANALYSIS, int((time.perf_counter()-_t0_dev)*1000), STATUS_ERROR)
        return jsonify({"error": str(e)}), 500


@app.route("/app-info", methods=["GET"])
def app_info():
    """Livrable #9 : info sur un package installé (mock ou ADB)."""
    package = request.args.get("package", "com.orange.otvp")
    serial  = request.args.get("serial", "")
    mode    = request.args.get("mode", "auto")

    _MOCK_PKGS = {
        "com.orange.otvp":      {"installed": True,  "version": "2.3.1", "permissions": 12},
        "com.orange.otvp.test": {"installed": True,  "version": "1.0.0", "permissions": 3},
        "com.android.settings": {"installed": True,  "version": "9.0",   "permissions": 5},
    }

    try:
        adb_ok = _adb_available() if mode != "mock" else False
        if adb_ok:
            from app_manager.app_installer import AppInstaller
            inst = AppInstaller()
            installed = inst.is_app_installed(package, serial or None)
            src = "adb-real"
        else:
            info_dict = _MOCK_PKGS.get(package, {"installed": False})
            installed  = info_dict.get("installed", False)
            src = "mock"

        result = {
            "package":   package,
            "serial":    serial or "auto",
            "installed": installed,
            "source":    src,
        }
        if src == "mock" and package in _MOCK_PKGS:
            result["version"]     = _MOCK_PKGS[package].get("version")
            result["permissions"] = _MOCK_PKGS[package].get("permissions")

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ============================================================
#   ROUTES MÉTRIQUES DE PERFORMANCE — LIVRABLE #8
# ============================================================

@app.route("/metrics", methods=["GET"])
def metrics_kpis():
    """KPIs agrégés : taux de succès, durée moyenne, total runs par opération."""
    kpis = get_kpis()
    kpis["metrics_enabled"] = _HAS_METRICS
    return jsonify(kpis)


@app.route("/metrics/history", methods=["GET"])
def metrics_history():
    """Liste des runs récents avec durée et statut."""
    operation = request.args.get("operation")
    limit = min(int(request.args.get("limit", 100)), 500)
    runs = get_runs(operation=operation, limit=limit)
    return jsonify({"runs": runs, "count": len(runs), "metrics_enabled": _HAS_METRICS})


@app.route("/metrics/clear", methods=["POST"])
def metrics_clear():
    """Supprime tous les enregistrements de métriques (ou d'une opération)."""
    operation = (request.json or {}).get("operation")
    deleted = clear_metrics(operation=operation)
    return jsonify({"deleted": deleted, "operation": operation or "all"})


# ============================================================
#   POINT D'ENTREE
# ============================================================

if __name__ == "__main__":
    print("Serveur demarre sur http://localhost:5000")
    app.run(debug=True, port=5000)
