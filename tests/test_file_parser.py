import unittest
import os
import tempfile
from analyzers.file_parser import PageObjectParser, FieldInfo


class TestFieldInfo(unittest.TestCase):
    """Tests pour la classe FieldInfo"""

    def test_field_info_creation(self):
        """Doit créer un FieldInfo avec les bons attributs"""
        field = FieldInfo(name="loginButton", annotation="@FindBy(id=\"login\")", line=10)
        self.assertEqual(field.name, "loginButton")
        self.assertEqual(field.line, 10)

    def test_field_info_repr(self):
        """Doit retourner une représentation lisible"""
        field = FieldInfo(name="loginButton", annotation="@FindBy(id=\"login\")", line=10)
        result = repr(field)
        self.assertIn("loginButton", result)
        self.assertIn("10", result)


class TestPageObjectParser(unittest.TestCase):
    """Tests pour la classe PageObjectParser"""

    def setUp(self):
        """Initialise le parser et un répertoire temporaire"""
        self.parser = PageObjectParser()
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Nettoie les fichiers temporaires"""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def _create_java_file(self, content: str) -> str:
        """Crée un fichier Java temporaire avec le contenu donné"""
        file_path = os.path.join(self.test_dir, "TestPage.java")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path

    # =========================================================
    # ✅ Tests parse()
    # =========================================================

    def test_parse_finds_findby_field(self):
        """Doit détecter un champ annoté avec @FindBy"""
        content = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        fields = self.parser.parse(file_path)
        self.assertEqual(len(fields), 1)
        self.assertEqual(fields[0].name, "loginButton")

    def test_parse_finds_android_findby_field(self):
        """Doit détecter un champ annoté avec @AndroidFindBy"""
        content = """
public class LoginPage {
    @AndroidFindBy(xpath = "//button[@id='login']")
    private MobileElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        fields = self.parser.parse(file_path)
        self.assertEqual(len(fields), 1)
        self.assertEqual(fields[0].name, "loginButton")

    def test_parse_finds_multiple_fields(self):
        """Doit détecter plusieurs champs annotés"""
        content = """
public class LoginPage {
    @FindBy(id = "login-btn")
    private WebElement loginButton;

    @FindBy(id = "username")
    private WebElement usernameField;

    @FindBy(id = "password")
    private WebElement passwordField;
}
"""
        file_path = self._create_java_file(content)
        fields = self.parser.parse(file_path)
        self.assertEqual(len(fields), 3)

    def test_parse_returns_empty_if_no_annotation(self):
        """Doit retourner une liste vide si aucune annotation"""
        content = """
public class LoginPage {
    private WebElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        fields = self.parser.parse(file_path)
        self.assertEqual(fields, [])

    def test_parse_ignores_annotation_without_field(self):
        """Doit ignorer une annotation sans champ sur la ligne suivante"""
        content = """
public class LoginPage {
    @FindBy(id = "login-btn")
    // commentaire au lieu d'un champ
}
"""
        file_path = self._create_java_file(content)
        fields = self.parser.parse(file_path)
        self.assertEqual(fields, [])

    def test_parse_detects_mobile_element(self):
        """Doit détecter un champ de type MobileElement"""
        content = """
public class LoginPage {
    @iOSFindBy(accessibility = "login")
    private MobileElement loginButton;
}
"""
        file_path = self._create_java_file(content)
        fields = self.parser.parse(file_path)
        self.assertEqual(len(fields), 1)

    # =========================================================
    # ✅ Tests extract_xpath()
    # =========================================================

    def test_extract_xpath_valid(self):
        """Doit extraire le XPath d'une annotation"""
        annotation = '@FindBy(xpath = "//button[@id=\'login\']")'
        result = self.parser.extract_xpath(annotation)
        self.assertEqual(result, "//button[@id='login']")

    def test_extract_xpath_no_xpath(self):
        """Doit retourner une chaîne vide si pas de XPath"""
        annotation = '@FindBy(id = "login-btn")'
        result = self.parser.extract_xpath(annotation)
        self.assertEqual(result, "")

    def test_extract_xpath_returns_string(self):
        """Doit toujours retourner une chaîne"""
        result = self.parser.extract_xpath("")
        self.assertIsInstance(result, str)

    # =========================================================
    # ✅ Tests extract_selector()
    # =========================================================

    def test_extract_selector_id(self):
        """Doit extraire un sélecteur de type id"""
        annotation = '@FindBy(id = "login-btn")'
        result = self.parser.extract_selector(annotation)
        self.assertEqual(result["type"], "id")
        self.assertEqual(result["value"], "login-btn")

    def test_extract_selector_xpath(self):
        """Doit extraire un sélecteur de type xpath"""
        annotation = '@FindBy(xpath = "//button")'
        result = self.parser.extract_selector(annotation)
        self.assertEqual(result["type"], "xpath")
        self.assertEqual(result["value"], "//button")

    def test_extract_selector_no_match(self):
        """Doit retourner un dict vide si aucun sélecteur"""
        result = self.parser.extract_selector("")
        self.assertEqual(result, {})

    def test_extract_selector_classname(self):
        """Doit extraire un sélecteur de type className"""
        annotation = '@FindBy(className = "btn-login")'
        result = self.parser.extract_selector(annotation)
        self.assertEqual(result["type"], "className")
        self.assertEqual(result["value"], "btn-login")

    # =========================================================
    # ✅ Tests is_static_field()
    # =========================================================

    def test_is_static_field_true(self):
        """Doit retourner True si le champ est static"""
        content = "private static WebElement loginButton;"
        file_path = self._create_java_file(content)
        result = self.parser.is_static_field(file_path, "loginButton")
        self.assertTrue(result)

    def test_is_static_field_false(self):
        """Doit retourner False si le champ n'est pas static"""
        content = "private WebElement loginButton;"
        file_path = self._create_java_file(content)
        result = self.parser.is_static_field(file_path, "loginButton")
        self.assertFalse(result)

    # =========================================================
    # ✅ Tests get_class_name()
    # =========================================================

    def test_get_class_name_found(self):
        """Doit retourner le nom de la classe Java"""
        content = "public class LoginPage {}"
        file_path = self._create_java_file(content)
        result = self.parser.get_class_name(file_path)
        self.assertEqual(result, "LoginPage")

    def test_get_class_name_not_found(self):
        """Doit retourner le nom du fichier si pas de classe"""
        content = "// pas de classe ici"
        file_path = self._create_java_file(content)
        result = self.parser.get_class_name(file_path)
        self.assertIn("TestPage", result)


if __name__ == '__main__':
    unittest.main()
