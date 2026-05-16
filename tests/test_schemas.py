import unittest
from pydantic import ValidationError
from models.schemas import (
    SeverityLevel, IssueType, Issue, FileReport, AnalysisReport
)


class TestSeverityLevel(unittest.TestCase):
    """Tests pour l'enum SeverityLevel"""

    def test_severity_critical_value(self):
        """CRITICAL doit avoir la valeur 'CRITICAL'"""
        self.assertEqual(SeverityLevel.CRITICAL, "CRITICAL")

    def test_severity_important_value(self):
        """IMPORTANT doit avoir la valeur 'IMPORTANT'"""
        self.assertEqual(SeverityLevel.IMPORTANT, "IMPORTANT")

    def test_severity_warning_value(self):
        """WARNING doit avoir la valeur 'WARNING'"""
        self.assertEqual(SeverityLevel.WARNING, "WARNING")

    def test_severity_info_value(self):
        """INFO doit avoir la valeur 'INFO'"""
        self.assertEqual(SeverityLevel.INFO, "INFO")

    def test_severity_all_values(self):
        """Doit contenir exactement 4 valeurs"""
        self.assertEqual(len(SeverityLevel), 4)


class TestIssueType(unittest.TestCase):
    """Tests pour l'enum IssueType"""

    def test_issue_type_duplicate_field(self):
        """DUPLICATE_FIELD doit avoir la bonne valeur"""
        self.assertEqual(IssueType.DUPLICATE_FIELD, "DUPLICATE_FIELD")

    def test_issue_type_invalid_annotation(self):
        """INVALID_ANNOTATION doit avoir la bonne valeur"""
        self.assertEqual(IssueType.INVALID_ANNOTATION, "INVALID_ANNOTATION")

    def test_issue_type_invalid_xpath(self):
        """INVALID_XPATH doit avoir la bonne valeur"""
        self.assertEqual(IssueType.INVALID_XPATH, "INVALID_XPATH")

    def test_issue_type_static_field(self):
        """STATIC_FIELD doit avoir la bonne valeur"""
        self.assertEqual(IssueType.STATIC_FIELD, "STATIC_FIELD")

    def test_issue_type_invalid_selector(self):
        """INVALID_SELECTOR doit avoir la bonne valeur"""
        self.assertEqual(IssueType.INVALID_SELECTOR, "INVALID_SELECTOR")

    def test_issue_type_all_values(self):
        """Doit contenir exactement 5 valeurs"""
        self.assertEqual(len(IssueType), 5)


class TestIssue(unittest.TestCase):
    """Tests pour le modèle Issue"""

    def _make_issue(self, **kwargs):
        """Crée une Issue avec des valeurs par défaut"""
        defaults = {
            "issue_type": IssueType.INVALID_XPATH,
            "severity": SeverityLevel.CRITICAL,
            "file": "LoginPage.java",
            "detail": "XPath invalide"
        }
        defaults.update(kwargs)
        return Issue(**defaults)

    def test_issue_creation_minimal(self):
        """Doit créer une Issue avec les champs obligatoires"""
        issue = self._make_issue()
        self.assertIsInstance(issue, Issue)

    def test_issue_required_field_issue_type(self):
        """issue_type est obligatoire"""
        with self.assertRaises(ValidationError):
            Issue(
                severity=SeverityLevel.CRITICAL,
                file="LoginPage.java",
                detail="XPath invalide"
            )

    def test_issue_required_field_severity(self):
        """severity est obligatoire"""
        with self.assertRaises(ValidationError):
            Issue(
                issue_type=IssueType.INVALID_XPATH,
                file="LoginPage.java",
                detail="XPath invalide"
            )

    def test_issue_required_field_file(self):
        """file est obligatoire"""
        with self.assertRaises(ValidationError):
            Issue(
                issue_type=IssueType.INVALID_XPATH,
                severity=SeverityLevel.CRITICAL,
                detail="XPath invalide"
            )

    def test_issue_required_field_detail(self):
        """detail est obligatoire"""
        with self.assertRaises(ValidationError):
            Issue(
                issue_type=IssueType.INVALID_XPATH,
                severity=SeverityLevel.CRITICAL,
                file="LoginPage.java"
            )

    def test_issue_optional_field_is_none_by_default(self):
        """field doit être None par défaut"""
        issue = self._make_issue()
        self.assertIsNone(issue.field)

    def test_issue_optional_line_is_none_by_default(self):
        """line doit être None par défaut"""
        issue = self._make_issue()
        self.assertIsNone(issue.line)

    def test_issue_optional_suggestion_is_none_by_default(self):
        """suggestion doit être None par défaut"""
        issue = self._make_issue()
        self.assertIsNone(issue.suggestion)

    def test_issue_with_all_fields(self):
        """Doit créer une Issue avec tous les champs"""
        issue = self._make_issue(
            field="loginButton",
            line=42,
            suggestion="Utiliser un id"
        )
        self.assertEqual(issue.field, "loginButton")
        self.assertEqual(issue.line, 42)
        self.assertEqual(issue.suggestion, "Utiliser un id")

    def test_issue_severity_is_enum(self):
        """severity doit être une instance de SeverityLevel"""
        issue = self._make_issue()
        self.assertIsInstance(issue.severity, SeverityLevel)

    def test_issue_type_is_enum(self):
        """issue_type doit être une instance de IssueType"""
        issue = self._make_issue()
        self.assertIsInstance(issue.issue_type, IssueType)


class TestFileReport(unittest.TestCase):
    """Tests pour le modèle FileReport"""

    def _make_file_report(self, **kwargs):
        """Crée un FileReport avec des valeurs par défaut"""
        defaults = {
            "file_name": "LoginPage.java",
            "file_path": "/project/LoginPage.java",
            "total_fields": 3,
            "issues": [],
            "is_valid": True
        }
        defaults.update(kwargs)
        return FileReport(**defaults)

    def test_file_report_creation(self):
        """Doit créer un FileReport valide"""
        report = self._make_file_report()
        self.assertIsInstance(report, FileReport)

    def test_file_report_required_file_name(self):
        """file_name est obligatoire"""
        with self.assertRaises(ValidationError):
            FileReport(
                file_path="/project/LoginPage.java",
                total_fields=3,
                issues=[],
                is_valid=True
            )

    def test_file_report_required_is_valid(self):
        """is_valid est obligatoire"""
        with self.assertRaises(ValidationError):
            FileReport(
                file_name="LoginPage.java",
                file_path="/project/LoginPage.java",
                total_fields=3,
                issues=[]
            )

    def test_file_report_is_valid_true(self):
        """is_valid doit pouvoir être True"""
        report = self._make_file_report(is_valid=True)
        self.assertTrue(report.is_valid)

    def test_file_report_is_valid_false(self):
        """is_valid doit pouvoir être False"""
        report = self._make_file_report(is_valid=False)
        self.assertFalse(report.is_valid)

    def test_file_report_issues_empty(self):
        """issues peut être une liste vide"""
        report = self._make_file_report(issues=[])
        self.assertEqual(report.issues, [])

    def test_file_report_with_issue(self):
        """issues peut contenir des Issue"""
        issue = Issue(
            issue_type=IssueType.INVALID_XPATH,
            severity=SeverityLevel.CRITICAL,
            file="LoginPage.java",
            detail="XPath invalide"
        )
        report = self._make_file_report(issues=[issue])
        self.assertEqual(len(report.issues), 1)

    def test_file_report_total_fields(self):
        """total_fields doit être correctement stocké"""
        report = self._make_file_report(total_fields=5)
        self.assertEqual(report.total_fields, 5)


class TestAnalysisReport(unittest.TestCase):
    """Tests pour le modèle AnalysisReport"""

    def _make_analysis_report(self, **kwargs):
        """Crée un AnalysisReport avec des valeurs par défaut"""
        defaults = {
            "project_path": "/project",
            "total_files": 0,
            "total_issues": 0,
            "critical_count": 0,
            "important_count": 0,
            "warning_count": 0,
            "files": [],
            "summary": "Analyse terminée"
        }
        defaults.update(kwargs)
        return AnalysisReport(**defaults)

    def test_analysis_report_creation(self):
        """Doit créer un AnalysisReport valide"""
        report = self._make_analysis_report()
        self.assertIsInstance(report, AnalysisReport)

    def test_analysis_report_required_project_path(self):
        """project_path est obligatoire"""
        with self.assertRaises(ValidationError):
            AnalysisReport(
                total_files=0,
                total_issues=0,
                critical_count=0,
                important_count=0,
                warning_count=0,
                files=[],
                summary="Analyse terminée"
            )

    def test_analysis_report_required_summary(self):
        """summary est obligatoire"""
        with self.assertRaises(ValidationError):
            AnalysisReport(
                project_path="/project",
                total_files=0,
                total_issues=0,
                critical_count=0,
                important_count=0,
                warning_count=0,
                files=[]
            )

    def test_analysis_report_counts(self):
        """Les compteurs doivent être correctement stockés"""
        report = self._make_analysis_report(
            total_files=5,
            total_issues=10,
            critical_count=3,
            important_count=4,
            warning_count=3
        )
        self.assertEqual(report.total_files, 5)
        self.assertEqual(report.total_issues, 10)
        self.assertEqual(report.critical_count, 3)
        self.assertEqual(report.important_count, 4)
        self.assertEqual(report.warning_count, 3)

    def test_analysis_report_files_empty(self):
        """files peut être une liste vide"""
        report = self._make_analysis_report(files=[])
        self.assertEqual(report.files, [])

    def test_analysis_report_summary(self):
        """summary doit être correctement stocké"""
        report = self._make_analysis_report(summary="3 problèmes détectés")
        self.assertEqual(report.summary, "3 problèmes détectés")


if __name__ == '__main__':
    unittest.main()
