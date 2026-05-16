import re
from typing import List
from utils.file_utils import read_file, get_file_name
from models.schemas import Issue, IssueType, SeverityLevel


class AnnotationChecker:
    """Verifie la validite des annotations Appium dans les Page Objects"""

    VALID_ANNOTATIONS = [
        'FindBy', 'AndroidFindBy', 'iOSFindBy',
        'iOSXCUITFindBy', 'FindBys', 'FindAll'
    ]

    # accessibility est un alias valide de accessibilityId dans Appium Java
    VALID_SELECTORS = [
        'id',
        'xpath',
        'className',
        'accessibilityId',
        'accessibility',        # alias Appium valide
        'name',
        'css',
        'tagName',
        'linkText',
        'partialLinkText',
        'androidUIAutomator',
        'iOSNsPredicate',
        'iOSClassChain',
        'uiAutomator',          # alias Android valide
        'predicate',            # alias iOS valide
        'classChain',           # alias iOS valide
        'value',                # utilise dans iOSXCUITFindBy
        'label',                # utilise dans iOSXCUITFindBy
    ]

    ANNOTATION_PATTERN = re.compile(
        r'@(?:FindBy|AndroidFindBy|iOSFindBy|iOSXCUITFindBy|FindBys|FindAll)'
        r'\s*\(([^)]+)\)',
        re.MULTILINE
    )

    # Pattern complet pour capturer aussi le nom de l'annotation
    ANNOTATION_FULL_PATTERN = re.compile(
        r'(@(?:FindBy|AndroidFindBy|iOSFindBy|iOSXCUITFindBy|FindBys|FindAll)'
        r'\s*\(([^)]+)\))',
        re.MULTILINE
    )

    def check(self, file_path: str) -> List[Issue]:
        """Verifie les annotations d'un fichier Java"""
        issues = []
        content = read_file(file_path)
        file_name = get_file_name(file_path)

        for match in self.ANNOTATION_FULL_PATTERN.finditer(content):
            annotation_full = match.group(1)
            annotation_body = match.group(2)
            line_num = content[:match.start()].count('\n') + 1

            # Verifier si l'annotation est vide
            empty_issues = self._check_empty_annotation(
                annotation_full, annotation_body,
                file_name, line_num
            )
            issues.extend(empty_issues)

            # Verifier les selecteurs valides
            selector_issues = self._check_valid_selector(
                annotation_full, annotation_body,
                file_name, line_num
            )
            issues.extend(selector_issues)

            # Verifier les valeurs vides
            value_issues = self._check_empty_value(
                annotation_full, annotation_body,
                file_name, line_num
            )
            issues.extend(value_issues)

            # Verifier les annotations mixtes
            mixed_issues = self._check_mixed_selectors(
                annotation_full, annotation_body,
                file_name, line_num
            )
            issues.extend(mixed_issues)

        return issues

    def _check_empty_annotation(
        self,
        annotation: str,
        body: str,
        file_name: str,
        line: int
    ) -> List[Issue]:
        """Verifie si l'annotation est vide"""
        issues = []
        if not body.strip():
            issues.append(Issue(
                issue_type=IssueType.INVALID_ANNOTATION,
                severity=SeverityLevel.CRITICAL,
                file=file_name,
                line=line,
                detail=(
                    f"Annotation vide detectee a la ligne {line} : "
                    f"{annotation[:80]}"
                ),
                suggestion=(
                    "Ajouter un selecteur valide dans l'annotation"
                )
            ))
        return issues

    def _check_valid_selector(
        self,
        annotation: str,
        body: str,
        file_name: str,
        line: int
    ) -> List[Issue]:
        """
        Verifie si le selecteur utilise est valide.
        Ignore les mots-cles Java comme 'group', 'using', etc.
        """
        issues = []

        # Extraire tous les selecteurs (mot = "valeur")
        selector_pattern = re.compile(r'(\w+)\s*=\s*"')
        matches = selector_pattern.findall(body)

        # Mots-cles Java a ignorer (pas des selecteurs)
        java_keywords = {
            'group', 'using', 'value', 'how', 'customFindBy',
            'androidKey', 'iOSKey', 'windowsKey'
        }

        for selector in matches:
            # Ignorer les mots-cles Java
            if selector in java_keywords:
                continue
            # Signaler uniquement les vrais selecteurs inconnus
            if selector not in self.VALID_SELECTORS:
                issues.append(Issue(
                    issue_type=IssueType.INVALID_SELECTOR,
                    severity=SeverityLevel.IMPORTANT,
                    file=file_name,
                    line=line,
                    detail=(
                        f"Selecteur inconnu '{selector}' "
                        f"a la ligne {line} : {annotation[:80]}"
                    ),
                    suggestion=(
                        f"Utiliser un selecteur valide parmi : "
                        f"{', '.join(self.VALID_SELECTORS)}"
                    )
                ))
        return issues

    def _check_empty_value(
        self,
        annotation: str,
        body: str,
        file_name: str,
        line: int
    ) -> List[Issue]:
        """Verifie si la valeur du selecteur est vide"""
        issues = []
        empty_value_pattern = re.compile(r'(\w+)\s*=\s*""')
        matches = empty_value_pattern.findall(body)

        for selector in matches:
            if selector in self.VALID_SELECTORS:
                issues.append(Issue(
                    issue_type=IssueType.INVALID_ANNOTATION,
                    severity=SeverityLevel.CRITICAL,
                    file=file_name,
                    line=line,
                    detail=(
                        f"Valeur vide pour le selecteur '{selector}' "
                        f"a la ligne {line} : {annotation[:80]}"
                    ),
                    suggestion=(
                        f"Fournir une valeur non vide "
                        f"pour le selecteur '{selector}'"
                    )
                ))
        return issues

    def _check_mixed_selectors(
        self,
        annotation: str,
        body: str,
        file_name: str,
        line: int
    ) -> List[Issue]:
        """Verifie si plusieurs selecteurs sont melanges"""
        issues = []
        selector_pattern = re.compile(r'(\w+)\s*=\s*"[^"]*"')
        matches = selector_pattern.findall(body)
        valid_matches = [
            m for m in matches
            if m in self.VALID_SELECTORS
        ]

        if len(valid_matches) > 1:
            issues.append(Issue(
                issue_type=IssueType.INVALID_ANNOTATION,
                severity=SeverityLevel.WARNING,
                file=file_name,
                line=line,
                detail=(
                    f"Plusieurs selecteurs detectes dans une meme "
                    f"annotation a la ligne {line} : "
                    f"{', '.join(valid_matches)}"
                ),
                suggestion=(
                    "Utiliser un seul selecteur par annotation @FindBy"
                )
            ))
        return issues
