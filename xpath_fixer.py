import re
import os
import shutil
from datetime import datetime


class XPathFixer:

    def __init__(self):
        self.fixed_count = 0
        self.backup_dir = "backups"

    # ============================================================
    #   SAUVEGARDE
    # ============================================================

    def create_backup(self, file_path):
        """Cree une sauvegarde du fichier avant correction"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = os.path.basename(file_path)
        backup_path = os.path.join(
            self.backup_dir, f"{file_name}.{timestamp}.bak"
        )
        shutil.copy2(file_path, backup_path)
        return backup_path

    # ============================================================
    #   CORRECTIONS DE BASE
    # ============================================================

    def fix_brackets(self, xpath):
        """Corrige les crochets non equilibres sur une chaine decodee"""
        open_count = xpath.count('[')
        close_count = xpath.count(']')
        if open_count > close_count:
            xpath = xpath + ']' * (open_count - close_count)
            print(f"[DEBUG] Ajout {open_count - close_count} crochet(s) ]")
        elif close_count > open_count:
            diff = close_count - open_count
            for _ in range(diff):
                last_idx = xpath.rfind(']')
                if last_idx != -1:
                    xpath = xpath[:last_idx] + xpath[last_idx + 1:]
            print(f"[DEBUG] Suppression {diff} crochet(s) ]")
        return xpath

    def fix_parentheses(self, xpath):
        """Corrige les parentheses non equilibrees sur une chaine decodee"""
        open_count = xpath.count('(')
        close_count = xpath.count(')')
        if open_count > close_count:
            xpath = xpath + ')' * (open_count - close_count)
            print(f"[DEBUG] Ajout {open_count - close_count} parenthese(s) )")
        elif close_count > open_count:
            diff = close_count - open_count
            for _ in range(diff):
                last_idx = xpath.rfind(')')
                if last_idx != -1:
                    xpath = xpath[:last_idx] + xpath[last_idx + 1:]
            print(f"[DEBUG] Suppression {diff} parenthese(s) )")
        return xpath

    # ============================================================
    #   EXTRACTION DU XPATH
    # ============================================================

    def extract_xpath_from_line(self, line):
        """
        Extrait le XPath brut d'une ligne Java.
        Supporte les formats :
          @iOSXCUITBy(xpath = "//*[@label=\"valeur\"]")
          @iOSXCUITFindBy(xpath = "...")
          @AndroidFindBy(xpath = "...")
          @FindBy(xpath = "...")
          xpath = "..."
          value = "..."
          accessibility = "..."
          Toute chaine contenant // ou [@
        """
        print(f"[DEBUG] Ligne brute : {repr(line.strip()[:120])}")

        # Patterns dans l'ordre de priorite
        patterns = [
            # xpath = "valeur" avec guillemets echappes
            (r'xpath\s*=\s*"((?:[^"\\]|\\.)*)"', "xpath="),
            # value = "valeur"
            (r'value\s*=\s*"((?:[^"\\]|\\.)*)"', "value="),
            # accessibility = "valeur"
            (r'accessibility\s*=\s*"((?:[^"\\]|\\.)*)"', "accessibility="),
            # Toute chaine entre guillemets contenant //
            (r'"((?:[^"\\]|\\.)*//(?:[^"\\]|\\.)*)"', "//"),
            # Toute chaine entre guillemets contenant [@
            (r'"((?:[^"\\]|\\.)*\[@(?:[^"\\]|\\.)*)"', "[@"),
        ]

        for pattern, label in patterns:
            match = re.search(pattern, line)
            if match:
                raw_value = match.group(1)
                # Decoder pour verifier les indicateurs XPath
                decoded = raw_value.replace('\\"', '"').replace("\\'", "'")
                xpath_indicators = ['//', '[@', '/*']
                if any(ind in decoded for ind in xpath_indicators):
                    print(f"[DEBUG] Pattern '{label}' match")
                    print(f"[DEBUG] Valeur brute   : {raw_value[:80]}")
                    print(f"[DEBUG] Valeur decodee : {decoded[:80]}")
                    # Retourner la valeur BRUTE et ses positions
                    return raw_value, match.start(1), match.end(1)

        print(f"[DEBUG] Aucun XPath detecte")
        return None, None, None

    # ============================================================
    #   CORRECTION DU XPATH
    # ============================================================

    def fix_xpath(self, raw_xpath):
        """
        Applique les corrections sur un XPath brut (avec guillemets echappes).
        1. Decode les echappements Java
        2. Corrige les crochets et parentheses
        3. Re-encode pour Java
        """
        original = raw_xpath

        # Decoder les echappements Java
        decoded = raw_xpath.replace('\\"', '"').replace("\\'", "'")
        print(f"[DEBUG] XPath decode : {decoded[:80]}")

        # Compter sur la version decodee
        open_brackets = decoded.count('[')
        close_brackets = decoded.count(']')
        open_parens = decoded.count('(')
        close_parens = decoded.count(')')

        print(f"[DEBUG] Crochets    : {open_brackets} [ / {close_brackets} ]")
        print(f"[DEBUG] Parentheses : {open_parens} ( / {close_parens} )")

        # Corriger sur la version decodee
        fixed = decoded
        fixed = self.fix_brackets(fixed)
        fixed = self.fix_parentheses(fixed)

        # Re-encoder les guillemets doubles pour Java
        fixed_encoded = fixed.replace('"', '\\"')

        changed = (original != fixed_encoded)
        print(f"[DEBUG] Modifie : {changed}")
        if changed:
            print(f"[DEBUG] Avant encode : {original[:80]}")
            print(f"[DEBUG] Apres encode : {fixed_encoded[:80]}")

        return fixed_encoded, changed

    # ============================================================
    #   CORRECTION D'UNE LIGNE
    # ============================================================

    def fix_line(self, line):
        """Corrige les XPath dans une ligne Java"""
        fixed_line = line
        was_fixed = False

        print(f"[DEBUG] Analyse ligne : {line.strip()[:100]}")

        raw_xpath, start, end = self.extract_xpath_from_line(line)

        if raw_xpath is not None:
            print(f"[DEBUG] XPath brut trouve : {raw_xpath[:80]}")
            fixed_xpath, changed = self.fix_xpath(raw_xpath)
            if changed:
                print(f"[DEBUG] XPath corrige : {fixed_xpath[:80]}")
                fixed_line = line[:start] + fixed_xpath + line[end:]
                was_fixed = True
            else:
                print(f"[DEBUG] Pas de changement necessaire")
        else:
            print(f"[DEBUG] Aucun XPath detecte dans cette ligne")

        return fixed_line, was_fixed

    # ============================================================
    #   CORRECTION D'UN FICHIER
    # ============================================================

    def fix_file(self, file_path, issues):
        """Corrige automatiquement un fichier Java"""
        if not os.path.exists(file_path):
            return {
                "success": False,
                "error": f"Fichier introuvable : {file_path}"
            }

        backup_path = self.create_backup(file_path)

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Collecter les numeros de lignes a corriger
        lines_to_fix = set()
        for issue in issues:
            line_num = issue.get('line')
            if line_num and line_num != '?':
                try:
                    lines_to_fix.add(int(line_num))
                except (ValueError, TypeError):
                    pass

        print(f"[DEBUG] Lignes a corriger : {sorted(lines_to_fix)}")
        print(f"[DEBUG] Total lignes fichier : {len(lines)}")

        fixed_lines = []
        corrections = []

        for idx, line in enumerate(lines):
            line_number = idx + 1
            if line_number in lines_to_fix:
                print(f"\n[DEBUG] === Traitement ligne {line_number} ===")
                fixed_line, was_fixed = self.fix_line(line)
                if was_fixed:
                    corrections.append({
                        "line": line_number,
                        "original": line.strip(),
                        "fixed": fixed_line.strip()
                    })
                    fixed_lines.append(fixed_line)
                    self.fixed_count += 1
                    print(f"[DEBUG] Ligne {line_number} corrigee !")
                else:
                    fixed_lines.append(line)
                    print(f"[DEBUG] Ligne {line_number} non corrigee")
            else:
                fixed_lines.append(line)

        # Ecrire le fichier corrige
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(fixed_lines)

        print(f"\n[DEBUG] Total corrections : {len(corrections)}")

        return {
            "success": True,
            "file": os.path.basename(file_path),
            "backup": backup_path,
            "corrections_count": len(corrections),
            "corrections": corrections
        }

    # ============================================================
    #   CORRECTION DE TOUS LES FICHIERS
    # ============================================================

    def fix_all_files(self, project_path, analysis_result):
        """Corrige tous les fichiers avec des problemes critiques"""
        issues = analysis_result.get("issues", [])
        files_with_issues = analysis_result.get("files_with_issues", [])
        results = []

        for file_info in files_with_issues:
            file_name = file_info.get("name")
            file_path = self.find_file(project_path, file_name)

            if not file_path:
                results.append({
                    "success": False,
                    "file": file_name,
                    "error": "Fichier introuvable dans le projet"
                })
                continue

            file_issues = [
                i for i in issues
                if i.get("file", "").lower() == file_name.lower()
                and i.get("severity") == "CRITICAL"
            ]

            if file_issues:
                result = self.fix_file(file_path, file_issues)
                results.append(result)

        return {
            "total_files_fixed": len([r for r in results if r.get("success")]),
            "total_corrections": self.fixed_count,
            "results": results
        }

    # ============================================================
    #   UTILITAIRES
    # ============================================================

    def find_file(self, project_path, file_name):
        """Recherche un fichier dans le projet (insensible a la casse)"""
        for root, dirs, files in os.walk(project_path):
            for f in files:
                if f.lower() == file_name.lower():
                    return os.path.join(root, f)
        return None

    def format_correction_report(self, fix_result):
        """Formate le rapport de correction"""
        if not fix_result.get("success"):
            return f"Erreur : {fix_result.get('error')}"

        file = fix_result.get("file")
        count = fix_result.get("corrections_count", 0)
        backup = fix_result.get("backup")
        corrections = fix_result.get("corrections", [])

        if count == 0:
            return (
                f"Aucune correction appliquee dans `{file}`.\n\n"
                f"Le XPath detecte est peut-etre dans un format "
                f"non standard.\n"
                f"Verifiez manuellement la ligne signalee."
            )

        response = f"OK `{file}` — {count} correction(s) appliquee(s) !\n\n"
        response += f"Sauvegarde creee : `{backup}`\n\n"
        response += "Detail des corrections :\n\n"

        for c in corrections:
            response += f"Ligne {c.get('line')} :\n"
            response += f"  Avant : `{c.get('original')[:100]}`\n"
            response += f"  Apres  : `{c.get('fixed')[:100]}`\n\n"

        return response