import unittest
import os
import tempfile
from models.schemas import AnalysisReport, FileReport, Issue, SeverityLevel, IssueType
from analyzers.report_generator import ReportGenerator


def make_issue(
    issue_type=IssueType.INVALID_XPATH,
    severity=SeverityLevel.CRITICAL,
    file="LoginPage.java",
    field="loginButton",
    line=10,
    detail="XPath invalide",
    suggestion="Utiliser un id"
):
    """Crée une Issue de test"""
    return Issue(
        issue_type=issue_type,
        severity=severity,
        file=file,
        field=field,
        line=line,
        detail=detail,
        suggestion=suggestion
    )


def make_file_report(file_name="LoginPage.java", issues=None, total_fields=3, is_valid=False):
    """Crée un FileReport de test"""
    return FileReport(
        file_name=file_name,
        file_path=f"/project/{file_name}",
        total_fields=total_fields,
        issues=issues or [],
        is_valid=is_valid
    )


def make_report(files=None, project_path="/project", summary="Analyse terminée"):
    """Crée un AnalysisReport de test"""
    files = files or []
    all_issues = [i for f in files for i in f.issues]
    return AnalysisReport(
        project_path=project_path,
        total_files=len(files),
        total_issues=len(all_issues),
        critical_count=sum(
            1 for i in all_issues if i.severity == SeverityLevel.CRITICAL
        ),
        important_count=sum(
            1 for i in all_issues if i.severity == SeverityLevel.IMPORTANT
        ),
        warning_count=sum(
            1 for i in all_issues if i.severity == SeverityLevel.WARNING
        ),
        files=files,
        summary=summary
    )


class TestReportGenerator(unittest.TestCase):
    """Tests pour ReportGenerator"""

    def setUp(self):
        """Crée un répertoire temporaire pour les rapports"""
        self.test_dir = tempfile.mkdtemp()
        self.generator = ReportGenerator(output_dir=self.test_dir)

    def tearDown(self):
        """Nettoie les fichiers temporaires"""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    # =========================================================
    # ✅ Tests generate()
    # =========================================================

    def test_generate_creates_text_file(self):
        """Doit créer un fichier texte dans le répertoire de sortie"""
        report = make_report()
        self.generator.generate(report)
        files = os.listdir(self.test_dir)
        txt_files = [f for f in files if f.endswith('.txt')]
        self.assertGreater(len(txt_files), 0)

    def test_generate_creates_json_file(self):
        """Doit créer un fichier JSON dans le répertoire de sortie"""
        report = make_report()
        self.generator.generate(report)
        files = os.listdir(self.test_dir)
        json_files = [f for f in files if f.endswith('.json')]
        self.assertGreater(len(json_files), 0)

    def test_generate_returns_string(self):
        """Doit retourner une chaîne de caractères"""
        report = make_report()
        result = self.generator.generate(report)
        self.assertIsInstance(result, str)

    def test_generate_with_issues(self):
        """Doit générer un rapport avec des issues"""
        issue = make_issue()
        file_report = make_file_report(issues=[issue])
        report = make_report(files=[file_report])
        result = self.generator.generate(report)
        self.assertIsInstance(result, str)

    # =========================================================
    # ✅ Tests _generate_text_report()
    # =========================================================

    def test_text_report_contains_project_path(self):
        """Le rapport texte doit contenir le chemin du projet"""
        report = make_report(project_path="/mon/projet")
        result = self.generator._generate_text_report(report)
        self.assertIn("/mon/projet", result)

    def test_text_report_contains_total_files(self):
        """Le rapport texte doit contenir le nombre de fichiers"""
        file_report = make_file_report()
        report = make_report(files=[file_report])
        result = self.generator._generate_text_report(report)
        self.assertIn("1", result)

    def test_text_report_contains_issue_detail(self):
        """Le rapport texte doit contenir le détail d'une issue"""
        issue = make_issue(detail="XPath trop fragile")
        file_report = make_file_report(issues=[issue])
        report = make_report(files=[file_report])
        result = self.generator._generate_text_report(report)
        self.assertIn("XPath trop fragile", result)

    def test_text_report_contains_field_name(self):
        """Le rapport texte doit contenir le nom du champ"""
        issue = make_issue(field="passwordField")
        file_report = make_file_report(issues=[issue])
        report = make_report(files=[file_report])
        result = self.generator._generate_text_report(report)
        self.assertIn("passwordField", result)

    def test_text_report_contains_suggestion(self):
        """Le rapport texte doit contenir la suggestion"""
        issue = make_issue(suggestion="Utiliser accessibility id")
        file_report = make_file_report(issues=[issue])
        report = make_report(files=[file_report])
        result = self.generator._generate_text_report(report)
        self.assertIn("Utiliser accessibility id", result)

    def test_text_report_no_issues_skips_file(self):
        """Le rapport texte doit ignorer les fichiers sans issues"""
        file_report = make_file_report(issues=[])
        report = make_report(files=[file_report])
        result = self.generator._generate_text_report(report)
        self.assertNotIn("LoginPage.java", result)

    # =========================================================
    # ✅ Tests _generate_json_report()
    # =========================================================

    def test_json_report_returns_string(self):
        """Le rapport JSON doit retourner une chaîne"""
        report = make_report()
        result = self.generator._generate_json_report(report)
        self.assertIsInstance(result, str)

    def test_json_report_is_valid_json(self):
        """Le rapport JSON doit être un JSON valide"""
        import json
        report = make_report()
        result = self.generator._generate_json_report(report)
        parsed = json.loads(result)
        self.assertIsInstance(parsed, dict)

    def test_json_report_contains_project_path(self):
        """Le rapport JSON doit contenir le chemin du projet"""
        import json
        report = make_report(project_path="/mon/projet")
        result = self.generator._generate_json_report(report)
        parsed = json.loads(result)
        self.assertEqual(parsed["project_path"], "/mon/projet")

    def test_json_report_contains_total_issues(self):
        """Le rapport JSON doit contenir le nombre total d'issues"""
        import json
        issue = make_issue()
        file_report = make_file_report(issues=[issue])
        report = make_report(files=[file_report])
        result = self.generator._generate_json_report(report)
        parsed = json.loads(result)
        self.assertEqual(parsed["total_issues"], 1)

    # =========================================================
    # ✅ Tests _get_severity_icon()
    # =========================================================

    def test_severity_icon_critical(self):
        """Doit retourner une icône pour CRITICAL"""
        result = self.generator._get_severity_icon(SeverityLevel.CRITICAL)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_severity_icon_important(self):
        """Doit retourner une icône pour IMPORTANT"""
        result = self.generator._get_severity_icon(SeverityLevel.IMPORTANT)
        self.assertIsInstance(result, str)

    def test_severity_icon_warning(self):
        """Doit retourner une icône pour WARNING"""
        result = self.generator._get_severity_icon(SeverityLevel.WARNING)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
