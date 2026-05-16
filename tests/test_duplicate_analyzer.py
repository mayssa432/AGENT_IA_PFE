import unittest
from unittest.mock import patch, MagicMock
from analyzers.duplicate_detector import DuplicateDetector
from models.schemas import IssueType, SeverityLevel


class TestDuplicateDetector(unittest.TestCase):
    """Tests pour le détecteur de doublons dans les Page Objects"""

    def setUp(self):
        self.detector = DuplicateDetector()

    # =========================================================
    # ✅ Tests SANS doublons
    # =========================================================

    def test_no_duplicate_no_issue(self):
        """Aucun doublon dans le fichier → 0 issue"""
        mock_fields = [
            MagicMock(name='loginBtn', line=5, annotation='@FindBy(id="login")'),
            MagicMock(name='passwordField', line=8, annotation='@FindBy(id="password")'),
        ]
        mock_fields[0].name = 'loginBtn'
        mock_fields[1].name = 'passwordField'

        with patch.object(self.detector.parser, 'parse', return_value=mock_fields):
            with patch('analyzers.duplicate_detector.read_file', return_value=''):
                with patch('analyzers.duplicate_detector.get_file_name', return_value='LoginPO.java'):
                    issues = self.detector.detect('LoginPO.java')

        duplicate_issues = [
            i for i in issues if i.issue_type == IssueType.DUPLICATE_FIELD
        ]
        self.assertEqual(len(duplicate_issues), 0)

    def test_no_static_field_no_issue(self):
        """Aucun champ static → 0 issue STATIC_FIELD"""
        content = (
            'private WebElement loginBtn;\n'
            'private WebElement passwordField;\n'
        )
        mock_fields = []

        with patch.object(self.detector.parser, 'parse', return_value=mock_fields):
            with patch('analyzers.duplicate_detector.read_file', return_value=content):
                with patch('analyzers.duplicate_detector.get_file_name', return_value='LoginPO.java'):
                    issues = self.detector.detect('LoginPO.java')

        static_issues = [
            i for i in issues if i.issue_type == IssueType.STATIC_FIELD
        ]
        self.assertEqual(len(static_issues), 0)

    # =========================================================
    # ❌ Tests AVEC doublons
    # =========================================================

    def test_duplicate_field_detected(self):
        """Même nom de champ déclaré 2 fois → issue DUPLICATE_FIELD"""
        mock_field_1 = MagicMock()
        mock_field_1.name = 'loginBtn'
        mock_field_1.line = 5
        mock_field_1.annotation = '@FindBy(id="login")'

        mock_field_2 = MagicMock()
        mock_field_2.name = 'loginBtn'
        mock_field_2.line = 12
        mock_field_2.annotation = '@FindBy(xpath="//*[@id=\'login\']")'

        mock_fields = [mock_field_1, mock_field_2]

        with patch.object(self.detector.parser, 'parse', return_value=mock_fields):
            with patch('analyzers.duplicate_detector.read_file', return_value=''):
                with patch('analyzers.duplicate_detector.get_file_name', return_value='LoginPO.java'):
                    issues = self.detector.detect('LoginPO.java')

        duplicate_issues = [
            i for i in issues if i.issue_type == IssueType.DUPLICATE_FIELD
        ]
        self.assertTrue(len(duplicate_issues) > 0)

    def test_duplicate_field_severity_critical(self):
        """Un doublon de champ a une sévérité CRITICAL"""
        mock_field_1 = MagicMock()
        mock_field_1.name = 'loginBtn'
        mock_field_1.line = 5
        mock_field_1.annotation = '@FindBy(id="login")'

        mock_field_2 = MagicMock()
        mock_field_2.name = 'loginBtn'
        mock_field_2.line = 12
        mock_field_2.annotation = '@FindBy(id="login")'

        mock_fields = [mock_field_1, mock_field_2]

        with patch.object(self.detector.parser, 'parse', return_value=mock_fields):
            with patch('analyzers.duplicate_detector.read_file', return_value=''):
                with patch('analyzers.duplicate_detector.get_file_name', return_value='LoginPO.java'):
                    issues = self.detector.detect('LoginPO.java')

        duplicate_issues = [
            i for i in issues if i.issue_type == IssueType.DUPLICATE_FIELD
        ]
        self.assertTrue(len(duplicate_issues) > 0)
        self.assertEqual(duplicate_issues[0].severity, SeverityLevel.CRITICAL)

    # =========================================================
    # ⚠️ Tests champs STATIC
    # =========================================================

    def test_static_field_detected(self):
        """Un champ static WebElement → issue STATIC_FIELD"""
        content = 'static WebElement loginBtn;\n'
        mock_fields = []

        with patch.object(self.detector.parser, 'parse', return_value=mock_fields):
            with patch('analyzers.duplicate_detector.read_file', return_value=content):
                with patch('analyzers.duplicate_detector.get_file_name', return_value='LoginPO.java'):
                    issues = self.detector.detect('LoginPO.java')

        static_issues = [
            i for i in issues if i.issue_type == IssueType.STATIC_FIELD
        ]
        self.assertTrue(len(static_issues) > 0)

    def test_static_field_severity_important(self):
        """Un champ static a une sévérité IMPORTANT"""
        content = 'static WebElement loginBtn;\n'
        mock_fields = []

        with patch.object(self.detector.parser, 'parse', return_value=mock_fields):
            with patch('analyzers.duplicate_detector.read_file', return_value=content):
                with patch('analyzers.duplicate_detector.get_file_name', return_value='LoginPO.java'):
                    issues = self.detector.detect('LoginPO.java')

        static_issues = [
            i for i in issues if i.issue_type == IssueType.STATIC_FIELD
        ]
        self.assertTrue(len(static_issues) > 0)
        self.assertEqual(static_issues[0].severity, SeverityLevel.IMPORTANT)

    def test_static_mobile_element_detected(self):
        """Un champ static MobileElement → issue STATIC_FIELD"""
        content = 'static MobileElement passwordField;\n'
        mock_fields = []

        with patch.object(self.detector.parser, 'parse', return_value=mock_fields):
            with patch('analyzers.duplicate_detector.read_file', return_value=content):
                with patch('analyzers.duplicate_detector.get_file_name', return_value='LoginPO.java'):
                    issues = self.detector.detect('LoginPO.java')

        static_issues = [
            i for i in issues if i.issue_type == IssueType.STATIC_FIELD
        ]
        self.assertTrue(len(static_issues) > 0)


if __name__ == '__main__':
    unittest.main()
