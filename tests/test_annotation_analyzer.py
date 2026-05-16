import unittest
from unittest.mock import patch
from analyzers.annotation_checker import AnnotationChecker
from models.schemas import IssueType, SeverityLevel


class TestAnnotationChecker(unittest.TestCase):
    """Tests pour l'analyseur d'annotations Appium"""

    def setUp(self):
        self.checker = AnnotationChecker()

    # =========================================================
    # ✅ Tests annotations VALIDES
    # =========================================================

    def test_valid_annotation_xpath(self):
        """@FindBy avec xpath valide ne génère pas d'issue"""
        content = '@FindBy(xpath = "//*[@resource-id=\'login\']")\nprivate WebElement loginBtn;'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        self.assertEqual(len(issues), 0)

    def test_valid_annotation_id(self):
        """@FindBy avec id valide ne génère pas d'issue"""
        content = '@FindBy(id = "com.orange:id/login_button")\nprivate WebElement loginBtn;'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        self.assertEqual(len(issues), 0)

    def test_valid_annotation_accessibility_id(self):
        """@AndroidFindBy avec accessibilityId valide ne génère pas d'issue"""
        content = '@AndroidFindBy(accessibilityId = "login_button")\nprivate WebElement loginBtn;'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        self.assertEqual(len(issues), 0)

    def test_no_annotation_no_issue(self):
        """Un fichier sans annotation ne génère pas d'issue"""
        content = 'public class LoginPO {\n    private WebElement loginBtn;\n}'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        self.assertEqual(len(issues), 0)

    # =========================================================
    # ❌ Tests annotations INVALIDES
    # =========================================================

    def test_empty_annotation_value(self):
        """@FindBy avec valeur vide génère une issue CRITICAL"""
        content = '@FindBy(xpath = "")\nprivate WebElement loginBtn;'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        self.assertTrue(len(issues) > 0)
        severities = [i.severity for i in issues]
        self.assertIn(SeverityLevel.CRITICAL, severities)

    def test_invalid_selector(self):
        """Un sélecteur inconnu génère une issue IMPORTANT"""
        content = '@FindBy(invalidSelector = "some_value")\nprivate WebElement loginBtn;'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        self.assertTrue(len(issues) > 0)
        severities = [i.severity for i in issues]
        self.assertIn(SeverityLevel.IMPORTANT, severities)

    def test_mixed_selectors(self):
        """Plusieurs sélecteurs dans une annotation génère une issue WARNING"""
        content = '@FindBy(xpath = "//*[@id=\'btn\']", id = "btn")\nprivate WebElement loginBtn;'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        self.assertTrue(len(issues) > 0)
        severities = [i.severity for i in issues]
        self.assertIn(SeverityLevel.WARNING, severities)

    def test_issue_type_invalid_annotation(self):
        """Le type d'issue est bien INVALID_ANNOTATION pour valeur vide"""
        content = '@FindBy(xpath = "")\nprivate WebElement loginBtn;'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        issue_types = [i.issue_type for i in issues]
        self.assertIn(IssueType.INVALID_ANNOTATION, issue_types)

    def test_issue_type_invalid_selector(self):
        """Le type d'issue est bien INVALID_SELECTOR pour sélecteur inconnu"""
        content = '@FindBy(badSelector = "value")\nprivate WebElement loginBtn;'
        with patch('analyzers.annotation_checker.read_file', return_value=content):
            with patch('analyzers.annotation_checker.get_file_name', return_value='LoginPO.java'):
                issues = self.checker.check('LoginPO.java')
        issue_types = [i.issue_type for i in issues]
        self.assertIn(IssueType.INVALID_SELECTOR, issue_types)


if __name__ == '__main__':
    unittest.main()
