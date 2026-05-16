import re
from typing import List, Dict
from utils.file_utils import read_file, get_file_name

class FieldInfo:
    """Représente un champ trouvé dans un Page Object Java"""

    def __init__(self, name: str, annotation: str, line: int):
        self.name = name
        self.annotation = annotation
        self.line = line

    def __repr__(self):
        return f"FieldInfo(name={self.name}, line={self.line})"


class PageObjectParser:
    """Parse un fichier Java Page Object et extrait les champs"""

    # Patterns de détection
    ANNOTATION_PATTERN = re.compile(
        r'@(FindBy|AndroidFindBy|iOSFindBy|FindBys|FindAll)\s*\(([^)]+)\)'
    )
    FIELD_PATTERN = re.compile(
        r'(private|public|protected)?\s*(static\s+)?'
        r'(WebElement|MobileElement|AndroidElement|List<\w+>)\s+(\w+)\s*;'
    )
    XPATH_PATTERN = re.compile(
        r'xpath\s*=\s*"([^"]+)"'
    )
    SELECTOR_PATTERN = re.compile(
        r'(id|xpath|className|accessibilityId|name|css)\s*=\s*"([^"]+)"'
    )

    def parse(self, file_path: str) -> List[FieldInfo]:
        """Parse un fichier Java et retourne la liste des champs"""
        content = read_file(file_path)
        lines = content.split('\n')
        fields = []

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Cherche une annotation
            annotation_match = self.ANNOTATION_PATTERN.search(line)
            if annotation_match:
                annotation = line

                # Cherche le champ sur la ligne suivante
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    field_match = self.FIELD_PATTERN.search(next_line)
                    if field_match:
                        field_name = field_match.group(4)
                        fields.append(FieldInfo(
                            name=field_name,
                            annotation=annotation,
                            line=i + 1
                        ))
            i += 1

        return fields

    def extract_xpath(self, annotation: str) -> str:
        """Extrait le XPath d'une annotation"""
        match = self.XPATH_PATTERN.search(annotation)
        return match.group(1) if match else ""

    def extract_selector(self, annotation: str) -> Dict[str, str]:
        """Extrait le sélecteur d'une annotation"""
        match = self.SELECTOR_PATTERN.search(annotation)
        if match:
            return {
                "type": match.group(1),
                "value": match.group(2)
            }
        return {}

    def is_static_field(self, file_path: str, field_name: str) -> bool:
        """Vérifie si un champ est déclaré static"""
        content = read_file(file_path)
        pattern = re.compile(
            rf'static\s+(WebElement|MobileElement)\s+{field_name}\s*;'
        )
        return bool(pattern.search(content))

    def get_class_name(self, file_path: str) -> str:
        """Retourne le nom de la classe Java"""
        content = read_file(file_path)
        match = re.search(r'class\s+(\w+)', content)
        return match.group(1) if match else get_file_name(file_path)
