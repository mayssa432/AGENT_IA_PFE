import unittest
import os
import tempfile
from analyzers.duplicate_detector import DuplicateDetector
from models.schemas import SeverityLevel, IssueType


class TestDuplicateDetector(unittest.TestCase):
    """Tests pour DuplicateDetector"""

    def setUp(self):
        """Initialise le détecteur et un répertoire temporaire"""
        self.detector = DuplicateDetector()
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Nettoie les fichiers temporaires"""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def _create_java_file(self, content: str, name: str = "TestPage.java") -> str:
        """Crée un fichier Java temporaire"""
        file_path = os.path.join(self.test_dir, name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path

    # =========================================================
    # ✅ Tests detect() — doublons dans un fichier
    # =========================================================

    def test_detect_no_duplicates(self):
        """Doit retourner une liste vide si pas de doublons"""
        content = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;

    @FindBy(id = "username")
    private WebElement usernameField;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector.detect(file_path)
        duplicate_issues = [
            i for i in issues if i.issue_type == IssueType.DUPLICATE_FIELD
        ]
        self.assertEqual(len(duplicate_issues), 0)

    def test_detect_one_duplicate(self):
        """Doit détecter un champ dupliqué"""
        content = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;

    @FindBy(id = "login-btn-2")
    private WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector.detect(file_path)
        duplicate_issues = [
            i for i in issues if i.issue_type == IssueType.DUPLICATE_FIELD
        ]
        self.assertEqual(len(duplicate_issues), 1)

    def test_detect_duplicate_severity_is_critical(self):
        """Un doublon doit avoir la sévérité CRITICAL"""
        content = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;

    @FindBy(id = "login-btn-2")
    private WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector.detect(file_path)
        duplicate_issues = [
            i for i in issues if i.issue_type == IssueType.DUPLICATE_FIELD
        ]
        self.assertEqual(duplicate_issues[0].severity, SeverityLevel.CRITICAL)

    def test_detect_duplicate_field_name(self):
        """L'issue doit contenir le nom du champ dupliqué"""
        content = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;

    @FindBy(id = "login-btn-2")
    private WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector.detect(file_path)
        duplicate_issues = [
            i for i in issues if i.issue_type == IssueType.DUPLICATE_FIELD
        ]
        self.assertEqual(duplicate_issues[0].field, "loginButton")

    def test_detect_multiple_duplicates(self):
        """Doit détecter plusieurs champs dupliqués"""
        content = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;

    @FindBy(id = "login-btn-2")
    private WebElement loginButton;

    @FindBy(id = "user")
    private WebElement usernameField;

    @FindBy(id = "user-2")
    private WebElement usernameField;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector.detect(file_path)
        duplicate_issues = [
            i for i in issues if i.issue_type == IssueType.DUPLICATE_FIELD
        ]
        self.assertEqual(len(duplicate_issues), 2)

    def test_detect_returns_list(self):
        """Doit toujours retourner une liste"""
        content = "public class LoginPage {}"
        file_path = self._create_java_file(content)
        result = self.detector.detect(file_path)
        self.assertIsInstance(result, list)

    # =========================================================
    # ✅ Tests _detect_static_fields()
    # =========================================================

    def test_detect_static_field(self):
        """Doit détecter un champ WebElement déclaré static"""
        content = """
public class LoginPage {
    private static WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        fields = []
        issues = self.detector._detect_static_fields(file_path, fields)
        static_issues = [
            i for i in issues if i.issue_type == IssueType.STATIC_FIELD
        ]
        self.assertEqual(len(static_issues), 1)

    def test_detect_static_field_severity_is_important(self):
        """Un champ static doit avoir la sévérité IMPORTANT"""
        content = """
public class LoginPage {
    private static WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector._detect_static_fields(file_path, [])
        self.assertEqual(issues[0].severity, SeverityLevel.IMPORTANT)

    def test_detect_static_field_name(self):
        """L'issue doit contenir le nom du champ static"""
        content = """
public class LoginPage {
    private static WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector._detect_static_fields(file_path, [])
        self.assertEqual(issues[0].field, "loginButton")

    def test_no_static_field(self):
        """Doit retourner une liste vide si pas de champ static"""
        content = """
public class LoginPage {
    private WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector._detect_static_fields(file_path, [])
        self.assertEqual(issues, [])

    def test_detect_mobile_element_static(self):
        """Doit détecter un MobileElement déclaré static"""
        content = """
public class LoginPage {
    private static MobileElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        issues = self.detector._detect_static_fields(file_path, [])
        self.assertEqual(len(issues), 1)

    # =========================================================
    # ✅ Tests detect_cross_file_duplicates()
    # =========================================================

    def test_cross_file_no_duplicates(self):
        """Doit retourner une liste vide si pas de doublons entre fichiers"""
        content1 = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;
}
"""
        content2 = """
public class HomePage {
    @FindBy(id = "home-btn")
    private WebElement homeButton;
}
"""
        file1 = self._create_java_file(content1, "LoginPage.java")
        file2 = self._create_java_file(content2, "HomePage.java")
        issues = self.detector.detect_cross_file_duplicates([file1, file2])
        self.assertEqual(issues, [])

    def test_cross_file_detects_duplicate(self):
        """Doit détecter un champ dupliqué entre deux fichiers"""
        content1 = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;
}
"""
        content2 = """
public class HomePage {
    @FindBy(id = "login-btn-2")
    private WebElement loginButton;
}
"""
        file1 = self._create_java_file(content1, "LoginPage.java")
        file2 = self._create_java_file(content2, "HomePage.java")
        issues = self.detector.detect_cross_file_duplicates([file1, file2])
        self.assertEqual(len(issues), 1)

    def test_cross_file_duplicate_severity_is_warning(self):
        """Un doublon inter-fichiers doit avoir la sévérité WARNING"""
        content1 = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;
}
"""
        content2 = """
public class HomePage {
    @FindBy(id = "login-btn-2")
    private WebElement loginButton;
}
"""
        file1 = self._create_java_file(content1, "LoginPage.java")
        file2 = self._create_java_file(content2, "HomePage.java")
        issues = self.detector.detect_cross_file_duplicates([file1, file2])
        self.assertEqual(issues[0].severity, SeverityLevel.WARNING)

    def test_cross_file_returns_list(self):
        """Doit toujours retourner une liste"""
        result = self.detector.detect_cross_file_duplicates([])
        self.assertIsInstance(result, list)

    def test_cross_file_empty_list(self):
        """Doit retourner une liste vide si aucun fichier fourni"""
        result = self.detector.detect_cross_file_duplicates([])
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
