import os
from typing import List
from colorama import Fore, Style, init
from utils.file_utils import get_java_files, get_file_name
from analyzer.file_parser import PageObjectParser
from analyzer.duplicate_detector import DuplicateDetector
from analyzer.annotation_checker import AnnotationChecker
from analyzer.xpath_validator import XPathValidator
from analyzer.report_generator import ReportGenerator
from models.schemas import (
    AnalysisReport, FileReport, SeverityLevel
)

init(autoreset=True)


class AppiumAgent:
    """Agent IA principal d'analyse des Page Objects Appium"""

    def __init__(self):
        self.parser = PageObjectParser()
        self.duplicate_detector = DuplicateDetector()
        self.annotation_checker = AnnotationChecker()
        self.xpath_validator = XPathValidator()
        self.report_generator = ReportGenerator()

    def analyze(self, project_path: str) -> AnalysisReport:
        """Lance l'analyse complète du projet"""

        print(Fore.CYAN + "\n" + "=" * 60)
        print(Fore.CYAN + "   🤖 AGENT IA - ANALYSE APPIUM PAGE OBJECTS")
        print(Fore.CYAN + "=" * 60)
        print(Fore.WHITE + f"📁 Projet : {project_path}\n")

        # Récupérer les fichiers Java
        java_files = get_java_files(project_path)

        if not java_files:
            print(Fore.YELLOW + "⚠️  Aucun fichier Java trouvé !")
            return self._empty_report(project_path)

        print(
            Fore.WHITE +
            f"📂 {len(java_files)} fichier(s) Java trouvé(s)\n"
        )

        file_reports = []
        all_issues_count = 0

        for file_path in java_files:
            file_name = get_file_name(file_path)
            print(Fore.WHITE + f"🔍 Analyse de : {file_name}")

            # Parser le fichier
            fields = self.parser.parse(file_path)
            issues = []

            # Détecter les doublons
            duplicate_issues = self.duplicate_detector.detect(file_path)
            issues.extend(duplicate_issues)

            # Vérifier les annotations
            annotation_issues = self.annotation_checker.check(file_path)
            issues.extend(annotation_issues)

            # Valider les XPath
            xpath_issues = self.xpath_validator.validate(file_path)
            issues.extend(xpath_issues)

            # Afficher le résultat
            if issues:
                print(
                    Fore.RED +
                    f"   ⚠️  {len(issues)} problème(s) détecté(s)"
                )
            else:
                print(Fore.GREEN + "   ✅ Aucun problème détecté")

            file_report = FileReport(
                file_name=file_name,
                file_path=file_path,
                total_fields=len(fields),
                issues=issues,
                is_valid=len(issues) == 0
            )
            file_reports.append(file_report)
            all_issues_count += len(issues)

        # Détecter les doublons inter-fichiers
        print(Fore.WHITE + "\n🔍 Analyse des doublons inter-fichiers...")
        cross_issues = self.duplicate_detector.detect_cross_file_duplicates(
            java_files
        )
        if cross_issues:
            print(
                Fore.YELLOW +
                f"   ⚠️  {len(cross_issues)} doublon(s) inter-fichiers"
            )
            if file_reports:
                file_reports[0].issues.extend(cross_issues)
                all_issues_count += len(cross_issues)
        else:
            print(Fore.GREEN + "   ✅ Aucun doublon inter-fichiers")

        # Compter par sévérité
        critical = sum(
            1 for fr in file_reports
            for i in fr.issues
            if i.severity == SeverityLevel.CRITICAL
        )
        important = sum(
            1 for fr in file_reports
            for i in fr.issues
            if i.severity == SeverityLevel.IMPORTANT
        )
        warning = sum(
            1 for fr in file_reports
            for i in fr.issues
            if i.severity == SeverityLevel.WARNING
        )

        # Créer le rapport
        report = AnalysisReport(
            project_path=project_path,
            total_files=len(java_files),
            total_issues=all_issues_count,
            critical_count=critical,
            important_count=important,
            warning_count=warning,
            files=file_reports,
            summary=""
        )

        # Générer le résumé
        report.summary = self.report_generator.generate_summary(report)

        # Afficher et sauvegarder le rapport
        print(Fore.CYAN + "\n" + "=" * 60)
        text_report = self.report_generator.generate(report)
        print(Fore.WHITE + "\n" + text_report)

        return report

    def _empty_report(self, project_path: str) -> AnalysisReport:
        """Retourne un rapport vide"""
        return AnalysisReport(
            project_path=project_path,
            total_files=0,
            total_issues=0,
            critical_count=0,
            important_count=0,
            warning_count=0,
            files=[],
            summary="Aucun fichier Java trouvé dans le projet."
        )


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Usage : python agent.py <chemin_projet>")
        print(Fore.YELLOW + "Exemple : python agent.py C:/MonProjet")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        print(Fore.RED + f"❌ Chemin introuvable : {project_path}")
        sys.exit(1)

    agent = AppiumAgent()
    agent.analyze(project_path)
