import json
import os
from datetime import datetime
from typing import List
from models.schemas import AnalysisReport, FileReport, Issue, SeverityLevel


class ReportGenerator:
    """Génère des rapports d'analyse au format texte et JSON"""

    def __init__(self, output_dir: str = "output/reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate(self, report: AnalysisReport) -> str:
        """Génère un rapport complet et le sauvegarde"""
        text_report = self._generate_text_report(report)
        json_report = self._generate_json_report(report)

        # Sauvegarder les rapports
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        text_path = os.path.join(
            self.output_dir, f"report_{timestamp}.txt"
        )
        json_path = os.path.join(
            self.output_dir, f"report_{timestamp}.json"
        )

        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(text_report)

        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(json_report)

        print(f"\n📄 Rapport texte sauvegardé : {text_path}")
        print(f"📄 Rapport JSON sauvegardé  : {json_path}")

        return text_report

    def _generate_text_report(self, report: AnalysisReport) -> str:
        """Génère le rapport au format texte"""
        lines = []
        lines.append("=" * 60)
        lines.append("       RAPPORT D'ANALYSE - AGENT IA APPIUM")
        lines.append("=" * 60)
        lines.append(f"📁 Projet    : {report.project_path}")
        lines.append(
            f"📅 Date      : "
            f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        lines.append(f"📂 Fichiers  : {report.total_files}")
        lines.append(f"⚠️  Problèmes : {report.total_issues}")
        lines.append("")
        lines.append("📊 RÉSUMÉ PAR SÉVÉRITÉ")
        lines.append("-" * 40)
        lines.append(f"🔴 CRITICAL  : {report.critical_count}")
        lines.append(f"🟠 IMPORTANT : {report.important_count}")
        lines.append(f"🟡 WARNING   : {report.warning_count}")
        lines.append("")
        lines.append("=" * 60)
        lines.append("📋 DÉTAIL PAR FICHIER")
        lines.append("=" * 60)

        for file_report in report.files:
            if not file_report.issues:
                continue

            lines.append(f"\n📄 {file_report.file_name}")
            lines.append(f"   Chemin : {file_report.file_path}")
            lines.append(
                f"   Champs : {file_report.total_fields} | "
                f"Problèmes : {len(file_report.issues)}"
            )
            lines.append("   " + "-" * 50)

            for issue in file_report.issues:
                icon = self._get_severity_icon(issue.severity)
                lines.append(
                    f"\n   {icon} [{issue.severity}] "
                    f"{issue.issue_type}"
                )
                if issue.field:
                    lines.append(f"   📌 Champ   : {issue.field}")
                if issue.line:
                    lines.append(f"   📍 Ligne   : {issue.line}")
                lines.append(f"   💬 Détail  : {issue.detail}")
                if issue.suggestion:
                    lines.append(
                        f"   💡 Conseil : {issue.suggestion}"
                    )

        lines.append("\n" + "=" * 60)
        lines.append("📝 RÉSUMÉ GLOBAL")
        lines.append("=" * 60)
        lines.append(report.summary)
        lines.append("=" * 60)

        return "\n".join(lines)

    def _generate_json_report(self, report: AnalysisReport) -> str:
        """Génère le rapport au format JSON"""
        return json.dumps(
            report.model_dump(),
            ensure_ascii=False,
            indent=2
        )

    def _get_severity_icon(self, severity: SeverityLevel) -> str:
        """Retourne l'icône correspondant à la sévérité"""
        icons = {
            SeverityLevel.CRITICAL: "🔴",
            SeverityLevel.IMPORTANT: "🟠",
            SeverityLevel.WARNING: "🟡",
            SeverityLevel.INFO: "🔵"
        }
        return icons.get(severity, "⚪")

    def generate_summary(self, report: AnalysisReport) -> str:
        """Génère un résumé court de l'analyse"""
        if report.total_issues == 0:
            return (
                "✅ Aucun problème détecté ! "
                "Le projet est conforme aux bonnes pratiques Appium."
            )

        summary_parts = []
        summary_parts.append(
            f"🔍 Analyse de {report.total_files} fichier(s) terminée."
        )
        summary_parts.append(
            f"⚠️  {report.total_issues} problème(s) détecté(s) :"
        )

        if report.critical_count > 0:
            summary_parts.append(
                f"  🔴 {report.critical_count} critique(s) à corriger "
                f"en priorité"
            )
        if report.important_count > 0:
            summary_parts.append(
                f"  🟠 {report.important_count} important(s) à traiter"
            )
        if report.warning_count > 0:
            summary_parts.append(
                f"  🟡 {report.warning_count} avertissement(s) "
                f"à examiner"
            )

        return "\n".join(summary_parts)
