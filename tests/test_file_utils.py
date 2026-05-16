import unittest
import os
import tempfile
from utils.file_utils import get_java_files, get_feature_files, read_file, get_file_name


class TestFileUtils(unittest.TestCase):
    """Tests pour les utilitaires de fichiers"""

    def setUp(self):
        """Crée un répertoire temporaire pour les tests"""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Nettoie les fichiers temporaires après chaque test"""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    # =========================================================
    # ✅ Tests get_java_files
    # =========================================================

    def test_get_java_files_returns_java_files(self):
        """Doit retourner les fichiers .java trouvés"""
        # Crée un fichier Java temporaire
        java_file = os.path.join(self.test_dir, 'LoginPage.java')
        with open(java_file, 'w') as f:
            f.write('public class LoginPage {}')

        result = get_java_files(self.test_dir)
        self.assertIn(java_file, result)

    def test_get_java_files_ignores_non_java(self):
        """Ne doit pas retourner les fichiers non .java"""
        txt_file = os.path.join(self.test_dir, 'readme.txt')
        with open(txt_file, 'w') as f:
            f.write('readme')

        result = get_java_files(self.test_dir)
        self.assertNotIn(txt_file, result)

    def test_get_java_files_ignores_target_dir(self):
        """Ne doit pas explorer le dossier target/"""
        target_dir = os.path.join(self.test_dir, 'target')
        os.makedirs(target_dir)
        java_file = os.path.join(target_dir, 'Compiled.java')
        with open(java_file, 'w') as f:
            f.write('public class Compiled {}')

        result = get_java_files(self.test_dir)
        self.assertNotIn(java_file, result)

    def test_get_java_files_ignores_git_dir(self):
        """Ne doit pas explorer le dossier .git/"""
        git_dir = os.path.join(self.test_dir, '.git')
        os.makedirs(git_dir)
        java_file = os.path.join(git_dir, 'Hook.java')
        with open(java_file, 'w') as f:
            f.write('public class Hook {}')

        result = get_java_files(self.test_dir)
        self.assertNotIn(java_file, result)

    def test_get_java_files_empty_dir(self):
        """Doit retourner une liste vide si aucun fichier Java"""
        result = get_java_files(self.test_dir)
        self.assertEqual(result, [])

    def test_get_java_files_multiple_files(self):
        """Doit retourner plusieurs fichiers Java"""
        for name in ['LoginPage.java', 'HomePage.java', 'BasePage.java']:
            with open(os.path.join(self.test_dir, name), 'w') as f:
                f.write(f'public class {name} {{}}')

        result = get_java_files(self.test_dir)
        self.assertEqual(len(result), 3)

    # =========================================================
    # ✅ Tests get_feature_files
    # =========================================================

    def test_get_feature_files_returns_feature_files(self):
        """Doit retourner les fichiers .feature trouvés"""
        feature_file = os.path.join(self.test_dir, 'login.feature')
        with open(feature_file, 'w') as f:
            f.write('Feature: Login')

        result = get_feature_files(self.test_dir)
        self.assertIn(feature_file, result)

    def test_get_feature_files_ignores_non_feature(self):
        """Ne doit pas retourner les fichiers non .feature"""
        java_file = os.path.join(self.test_dir, 'LoginPage.java')
        with open(java_file, 'w') as f:
            f.write('public class LoginPage {}')

        result = get_feature_files(self.test_dir)
        self.assertNotIn(java_file, result)

    def test_get_feature_files_ignores_target_dir(self):
        """Ne doit pas explorer le dossier target/"""
        target_dir = os.path.join(self.test_dir, 'target')
        os.makedirs(target_dir)
        feature_file = os.path.join(target_dir, 'login.feature')
        with open(feature_file, 'w') as f:
            f.write('Feature: Login')

        result = get_feature_files(self.test_dir)
        self.assertNotIn(feature_file, result)

    def test_get_feature_files_empty_dir(self):
        """Doit retourner une liste vide si aucun fichier .feature"""
        result = get_feature_files(self.test_dir)
        self.assertEqual(result, [])

    # =========================================================
    # ✅ Tests read_file
    # =========================================================

    def test_read_file_utf8(self):
        """Doit lire un fichier encodé en UTF-8"""
        file_path = os.path.join(self.test_dir, 'test.java')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('public class Test {}')

        result = read_file(file_path)
        self.assertEqual(result, 'public class Test {}')

    def test_read_file_latin1(self):
        """Doit lire un fichier encodé en latin-1"""
        file_path = os.path.join(self.test_dir, 'test_latin.java')
        with open(file_path, 'w', encoding='latin-1') as f:
            f.write('// commentaire avec accent : éàü')

        result = read_file(file_path)
        self.assertIn('commentaire', result)

    def test_read_file_returns_string(self):
        """Doit retourner une chaîne de caractères"""
        file_path = os.path.join(self.test_dir, 'test.java')
        with open(file_path, 'w') as f:
            f.write('content')

        result = read_file(file_path)
        self.assertIsInstance(result, str)

    # =========================================================
    # ✅ Tests get_file_name
    # =========================================================

    def test_get_file_name_simple(self):
        """Doit retourner le nom du fichier sans le chemin"""
        result = get_file_name('C:/Users/test/LoginPage.java')
        self.assertEqual(result, 'LoginPage.java')

    def test_get_file_name_with_extension(self):
        """Doit conserver l'extension du fichier"""
        result = get_file_name('/home/user/project/login.feature')
        self.assertEqual(result, 'login.feature')

    def test_get_file_name_only_filename(self):
        """Doit retourner le nom si pas de chemin"""
        result = get_file_name('BasePage.java')
        self.assertEqual(result, 'BasePage.java')


if __name__ == '__main__':
    unittest.main()
