import re
from typing import List, Dict
from utils.file_utils import read_file, get_file_name
from analyzers.file_parser import PageObjectParser, FieldInfo
from models.schemas import Issue, IssueType, SeverityLevel


class DuplicateDetector:
    """Détecte les champs dupliqués dans les Page Objects Java"""

    def __init__(self):
        self.parser = PageObjectParser()

    def detect(self, file_path: str) -> List[Issue]:
        """Détecte les doublons dans un fichier Java"""
        issues = []
        fields = self.parser.parse(file_path)
        file_name = get_file_name(file_path)

        # Regrouper les champs par nom
        field_map: Dict[str, List[FieldInfo]] = {}
        for field in fields:
            if field.name not in field_map:
                field_map[field.name] = []
            field_map[field.name].append(field)

        # Détecter les doublons
        for field_name, occurrences in field_map.items():
            if len(occurrences) > 1:
                lines = [str(o.line) for o in occurrences]
                issue = Issue(
                    issue_type=IssueType.DUPLICATE_FIELD,
                    severity=SeverityLevel.CRITICAL,
                    file=file_name,
                    field=field_name,
                    line=occurrences[0].line,
                    detail=(
                        f"Le champ '{field_name}' est déclaré "
                        f"{len(occurrences)} fois "
                        f"(lignes : {', '.join(lines)})"
                    ),
                    suggestion=(
                        f"Garder une seule déclaration de '{field_name}' "
                        f"et supprimer les doublons"
                    )
                )
                issues.append(issue)

        # Détecter les champs static
        static_issues = self._detect_static_fields(file_path, fields)
        issues.extend(static_issues)

        return issues

    def _detect_static_fields(
        self,
        file_path: str,
        fields: List[FieldInfo]
    ) -> List[Issue]:
        """Détecte les champs WebElement déclarés static"""
        issues = []
        content = read_file(file_path)
        file_name = get_file_name(file_path)

        static_pattern = re.compile(
            r'static\s+(WebElement|MobileElement|AndroidElement)\s+(\w+)\s*;'
        )

        for match in static_pattern.finditer(content):
            field_name = match.group(2)
            line_num = content[:match.start()].count('\n') + 1

            issue = Issue(
                issue_type=IssueType.STATIC_FIELD,
                severity=SeverityLevel.IMPORTANT,
                file=file_name,
                field=field_name,
                line=line_num,
                detail=(
                    f"Le champ '{field_name}' est déclaré static. "
                    f"Les WebElements ne doivent pas être static "
                    f"dans un Page Object"
                ),
                suggestion=(
                    f"Supprimer le mot-clé 'static' "
                    f"de la déclaration de '{field_name}'"
                )
            )
            issues.append(issue)

        return issues

    def detect_cross_file_duplicates(
        self,
        file_paths: List[str]
    ) -> List[Issue]:
        """Détecte les doublons entre plusieurs fichiers"""
        issues = []
        all_fields: Dict[str, List[Dict]] = {}

        for file_path in file_paths:
            fields = self.parser.parse(file_path)
            file_name = get_file_name(file_path)

            for field in fields:
                key = field.name
                if key not in all_fields:
                    all_fields[key] = []
                all_fields[key].append({
                    "file": file_name,
                    "line": field.line,
                    "annotation": field.annotation
                })

        for field_name, occurrences in all_fields.items():
            if len(occurrences) > 1:
                files = list(set([o["file"] for o in occurrences]))
                if len(files) > 1:
                    issue = Issue(
                        issue_type=IssueType.DUPLICATE_FIELD,
                        severity=SeverityLevel.WARNING,
                        file=files[0],
                        field=field_name,
                        detail=(
                            f"Le champ '{field_name}' existe "
                            f"dans plusieurs fichiers : "
                            f"{', '.join(files)}"
                        ),
                        suggestion=(
                            f"Vérifier si '{field_name}' "
                            f"doit être mutualisé dans une classe parente"
                        )
                    )
                    issues.append(issue)

        return issues
