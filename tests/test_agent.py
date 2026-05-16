import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock

class TestAgent(unittest.TestCase):

    def test_valid_path_exists(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.assertTrue(os.path.exists(path))

    def test_invalid_path(self):
        path = "C:\\invalid\\path\\that\\does\\not\\exist"
        self.assertFalse(os.path.exists(path))

    def test_java_files_detection(self):
        test_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        java_files = []
        for root, dirs, files in os.walk(test_dir):
            for file in files:
                if file.endswith('.java'):
                    java_files.append(file)
        self.assertIsInstance(java_files, list)

if __name__ == '__main__':
    unittest.main()

