from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
import re
import json
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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

        return jsonify(result)

    except Exception as e:
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
#   POINT D'ENTREE
# ============================================================

if __name__ == "__main__":
    print("Serveur demarre sur http://localhost:5000")
    app.run(debug=True, port=5000)
