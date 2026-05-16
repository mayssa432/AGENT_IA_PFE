import re
from typing import List
from utils.file_utils import read_file, get_file_name
from models.schemas import Issue, IssueType, SeverityLevel


class XPathAnalyzer:
    """Valide les expressions XPath dans les Page Objects Java"""

    # Pattern corrige : supporte les guillemets echappes \"
    XPATH_PATTERN = re.compile(
        r'xpath\s*=\s*"((?:[^"\\]|\\.)*)"'
    )

    # Patterns XPath suspects
    ABSOLUTE_XPATH_PATTERN = re.compile(r'^/html|^/body')
    LONG_XPATH_PATTERN = re.compile(r'(/\w+){6,}')
    INDEX_PATTERN = re.compile(r'$$\d+$$')
    CONTAINS_PATTERN = re.compile(r'contains\s*\(')
    TEXT_PATTERN = re.compile(r'text\(\)')
    SPECIAL_CHARS_PATTERN = re.compile(r'[#!?]{2,}')

    def validate(self, file_path: str) -> List[Issue]:
        """Valide tous les XPath d'un fichier Java"""
        issues = []
        content = read_file(file_path)
        file_name = get_file_name(file_path)

        for match in self.XPATH_PATTERN.finditer(content):
            # Valeur brute avec echappements Java
            raw_xpath = match.group(1)
            # Decoder pour l'analyse
            xpath = raw_xpath.replace('\\"', '"').replace("\\'", "'")
            line_num = content[:match.start()].count('\n') + 1

            print(f"[XPATH] Ligne {line_num} : {xpath[:80]}")

            absolute_issues = self._check_absolute_xpath(
                xpath, file_name, line_num
            )
            issues.extend(absolute_issues)

            long_issues = self._check_long_xpath(
                xpath, file_name, line_num
            )
            issues.extend(long_issues)

            index_issues = self._check_index_xpath(
                xpath, file_name, line_num
            )
            issues.extend(index_issues)

            # Passer le xpath DECODE a _check_syntax
            syntax_issues = self._check_syntax(
                xpath, file_name, line_num
            )
            issues.extend(syntax_issues)

            text_issues = self._check_text_xpath(
                xpath, file_name, line_num
            )
            issues.extend(text_issues)

        return issues

    def _check_absolute_xpath(
        self, xpath: str, file_name: str, line: int
    ) -> List[Issue]:
        issues = []
        if self.ABSOLUTE_XPATH_PATTERN.search(xpath):
            issues.append(Issue(
                issue_type=IssueType.INVALID_XPATH,
                severity=SeverityLevel.CRITICAL,
                file=file_name,
                line=line,
                detail=(
                    f"XPath absolu detecte a la ligne {line} : "
                    f"'{xpath[:50]}'. Les XPath absolus sont fragiles"
                ),
                suggestion=(
                    "Utiliser un XPath relatif commencant par '//' "
                    "avec des attributs stables comme @resource-id"
                )
            ))
        return issues

    def _check_long_xpath(
        self, xpath: str, file_name: str, line: int
    ) -> List[Issue]:
        issues = []
        if self.LONG_XPATH_PATTERN.search(xpath):
            issues.append(Issue(
                issue_type=IssueType.INVALID_XPATH,
                severity=SeverityLevel.IMPORTANT,
                file=file_name,
                line=line,
                detail=(
                    f"XPath trop long detecte a la ligne {line} : "
                    f"'{xpath[:50]}'. Plus de 5 niveaux = fragile"
                ),
                suggestion=(
                    "Simplifier le XPath en utilisant des attributs "
                    "uniques comme @resource-id ou @content-desc"
                )
            ))
        return issues

    def _check_index_xpath(
        self, xpath: str, file_name: str, line: int
    ) -> List[Issue]:
        issues = []
        if self.INDEX_PATTERN.search(xpath):
            issues.append(Issue(
                issue_type=IssueType.INVALID_XPATH,
                severity=SeverityLevel.IMPORTANT,
                file=file_name,
                line=line,
                detail=(
                    f"XPath avec index numerique a la ligne {line} : "
                    f"'{xpath[:50]}'. Les index dependent de l'ordre du DOM"
                ),
                suggestion=(
                    "Remplacer l'index par un attribut unique "
                    "comme @resource-id ou @text"
                )
            ))
        return issues

    def _check_syntax(
        self, xpath: str, file_name: str, line: int
    ) -> List[Issue]:
        """
        Verifie les crochets et parentheses sur le XPath DECODE.
        Le xpath recu ici est deja decode (sans les echappements Java).
        """
        issues = []

        open_parens = xpath.count('(')
        close_parens = xpath.count(')')
        open_brackets = xpath.count('[')
        close_brackets = xpath.count(']')

        print(
            f"[SYNTAX] Ligne {line} — "
            f"( {open_parens}/{close_parens} "
            f"[ {open_brackets}/{close_brackets}"
        )

        if open_parens != close_parens:
            issues.append(Issue(
                issue_type=IssueType.INVALID_XPATH,
                severity=SeverityLevel.CRITICAL,
                file=file_name,
                line=line,
                detail=(
                    f"XPath avec parentheses non equilibrees "
                    f"a la ligne {line} : '{xpath[:50]}'"
                ),
                suggestion=(
                    "Verifier et corriger les parentheses du XPath"
                )
            ))

        if open_brackets != close_brackets:
            issues.append(Issue(
                issue_type=IssueType.INVALID_XPATH,
                severity=SeverityLevel.CRITICAL,
                file=file_name,
                line=line,
                detail=(
                    f"XPath avec crochets non equilibres "
                    f"a la ligne {line} : '{xpath[:50]}'"
                ),
                suggestion=(
                    "Verifier et corriger les crochets du XPath"
                )
            ))

        return issues

    def _check_text_xpath(
        self, xpath: str, file_name: str, line: int
    ) -> List[Issue]:
        issues = []
        if self.TEXT_PATTERN.search(xpath):
            issues.append(Issue(
                issue_type=IssueType.INVALID_XPATH,
                severity=SeverityLevel.WARNING,
                file=file_name,
                line=line,
                detail=(
                    f"Utilisation de text() dans un XPath mobile "
                    f"a la ligne {line} : '{xpath[:50]}'. "
                    f"text() n'est pas fiable sur mobile"
                ),
                suggestion=(
                    "Remplacer text() par @text ou @content-desc "
                    "pour les applications mobiles Appium"
                )
            ))
        return issues

    def is_valid_xpath(self, xpath: str) -> bool:
        """Verifie si une expression XPath est valide"""
        if not xpath:
            return False
        # Decoder avant de verifier
        decoded = xpath.replace('\\"', '"').replace("\\'", "'")
        if decoded.count('(') != decoded.count(')'):
            return False
        if decoded.count('[') != decoded.count(']'):
            return False
        if self.SPECIAL_CHARS_PATTERN.search(decoded):
            return False
        return True
