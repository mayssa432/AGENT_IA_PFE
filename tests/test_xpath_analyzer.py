import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from analyzers.xpath_analyzer import XPathAnalyzer

class TestXPathAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = XPathAnalyzer()

    # ✅ Valid XPath tests
    def test_valid_xpath_id(self):
        result = self.analyzer.is_valid_xpath('//*[@id="login_button"]')
        self.assertTrue(result)

    def test_valid_xpath_text(self):
        result = self.analyzer.is_valid_xpath('//*[@text="Submit"]')
        self.assertTrue(result)

    def test_valid_xpath_contains(self):
        result = self.analyzer.is_valid_xpath('//*[contains(@text,"Login")]')
        self.assertTrue(result)

    # ❌ Invalid XPath tests
    def test_invalid_xpath_empty(self):
        result = self.analyzer.is_valid_xpath('')
        self.assertFalse(result)

    def test_invalid_xpath_unbalanced_brackets(self):
        result = self.analyzer.is_valid_xpath('//*[@id="login"')
        self.assertFalse(result)

    def test_invalid_xpath_unbalanced_parentheses(self):
        result = self.analyzer.is_valid_xpath('//*[contains(@text,"Login"')
        self.assertFalse(result)

    def test_invalid_xpath_none(self):
        result = self.analyzer.is_valid_xpath(None)
        self.assertFalse(result)

    def test_invalid_xpath_special_chars(self):
        result = self.analyzer.is_valid_xpath('//*[@id="###"]')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
