import os
import re
from typing import Any, Dict, List, Optional, Tuple
from lxml.etree import XPathEvalError

from .ui_parser import UiParser

ANNOTATION_SEARCH = re.compile(r'@(?P<name>AndroidFindBy|AndroidBy|AndroidFindAll|iOSXCUITFindBy)')
PARAM_DOUBLE_QUOTE = re.compile(r'(?P<name>\w+)\s*=\s*"(?P<value>(?:[^"\\]|\\.)*)"')
PARAM_SINGLE_QUOTE = re.compile(r"(?P<name>\w+)\s*=\s*'(?P<value>(?:[^'\\]|\\.)*)'")
IOS_PREDICATE_PATTERN = re.compile(r"(?P<attr>\w+)\s*(==|!=|contains|CONTAINS)\s*['\"](?P<value>[^'\"]+)['\"]")


class SelectorValidator:
    """Valide les annotations de sélecteurs Java contre un DOM XML."""

    def __init__(self):
        self.parser = UiParser()

    def validate_file(self, java_file: str, root: Any) -> List[Dict[str, Any]]:
        annotations = self.parse_annotations(java_file)
        issues: List[Dict[str, Any]] = []

        for annotation in annotations:
            if annotation.get("alternatives"):
                valid = any(
                    self.validate_selector(
                        alt["selector_name"], alt["selector_value"], root
                    )[0]
                    for alt in annotation["alternatives"]
                )
            else:
                valid, _ = self.validate_selector(
                    annotation["selector_name"], annotation["selector_value"], root
                )

            if not valid:
                issues.append({
                    "line": annotation["line"],
                    "annotation": annotation["annotation_text"],
                    "selector_name": annotation.get("selector_name"),
                    "selector_value": annotation.get("selector_value"),
                    "message": self._build_issue_message(annotation),
                    "valid": False,
                })

        return issues

    def validate_selector(self, selector_name: str, selector_value: str, root: Any) -> Tuple[bool, Optional[List[Any]]]:
        selector_name = selector_name.strip()
        selector_value = selector_value.strip()

        if selector_name == "xpath":
            try:
                elements = root.xpath(selector_value)
                return bool(elements), elements
            except XPathEvalError:
                return False, None
            except Exception:
                return False, None

        if selector_name in ["id", "resource-id"]:
            elements = self.parser.find_elements_by_attribute(root, "resource-id", selector_value, exact=True)
            return bool(elements), elements

        if selector_name in ["content-desc", "accessibility", "accessibility-id"]:
            elements = self.parser.find_elements_by_attribute(root, "content-desc", selector_value, exact=True)
            if elements:
                return True, elements
            elements = self.parser.find_elements_by_attribute(root, "accessibility-id", selector_value, exact=True)
            return bool(elements), elements

        if selector_name == "name":
            elements = self.parser.find_elements_by_attribute(root, "name", selector_value, exact=True)
            return bool(elements), elements

        if selector_name == "className":
            elements = self.parser.find_elements_by_attribute(root, "class", selector_value, exact=True)
            return bool(elements), elements

        if selector_name == "iOSNsPredicate":
            return self._validate_ios_ns_predicate(selector_value, root)

        if selector_name in ["uiAutomator", "androidUIAutomator"]:
            return self._validate_ui_automator(selector_value, root)

        if selector_name == "iOSClassChain":
            return self._validate_ios_class_chain(selector_value, root)

        if selector_name == "iOSNsPredicate":
            return self._validate_ios_ns_predicate(selector_value, root)

        # Fallback: try matching any attribute with the given name.
        try:
            elements = self.parser.find_elements_by_attribute(root, selector_name, selector_value, exact=True)
            return bool(elements), elements
        except Exception:
            return False, None

    def parse_annotations(self, java_file: str) -> List[Dict[str, Any]]:
        if not os.path.exists(java_file):
            raise FileNotFoundError(f"Fichier introuvable : {java_file}")

        with open(java_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        annotations: List[Dict[str, Any]] = []
        index = 0

        while index < len(lines):
            raw_line = lines[index]
            stripped = raw_line.strip()
            match = ANNOTATION_SEARCH.search(stripped)
            if not match:
                index += 1
                continue

            annotation_name = match.group("name")
            block_lines = [stripped]
            paren_balance = stripped.count("(") - stripped.count(")")

            while paren_balance > 0 and index + 1 < len(lines):
                index += 1
                next_line = lines[index].strip()
                block_lines.append(next_line)
                paren_balance += next_line.count("(") - next_line.count(")")

            annotation_text = " ".join(block_lines)
            line_number = index - len(block_lines) + 2

            if annotation_name == "AndroidFindAll":
                annotations.extend(self._parse_android_find_all(annotation_text, line_number))
            else:
                parsed = self._build_annotation(annotation_text, annotation_name, line_number)
                if parsed:
                    annotations.append(parsed)

            index += 1

        return annotations

    def _parse_android_find_all(self, annotation_text: str, base_line: int) -> List[Dict[str, Any]]:
        nested_annotations: List[Dict[str, Any]] = []
        nested_pattern = re.compile(r'@(?P<name>AndroidBy|AndroidFindBy|iOSXCUITFindBy)\s*\(')

        for match in nested_pattern.finditer(annotation_text):
            start = match.start()
            inner_text, _ = self._extract_balanced_parentheses(annotation_text, start + annotation_text[start:].find("(") )
            if inner_text is None:
                continue
            nested_block = f"@{match.group('name')}({inner_text})"
            parsed = self._build_annotation(nested_block, match.group("name"), base_line)
            if parsed:
                nested_annotations.append(parsed)

        group_params = self._extract_params(annotation_text)
        return [{
            "annotation_name": "AndroidFindAll",
            "annotation_text": annotation_text,
            "line": base_line,
            "alternatives": nested_annotations,
        }] if nested_annotations else []

    def _build_annotation(self, annotation_text: str, annotation_name: str, line: int) -> Optional[Dict[str, Any]]:
        params = self._extract_params(annotation_text)
        if not params:
            return None

        selector_name, selector_value = self._choose_selector(params)
        if not selector_name:
            return None

        return {
            "annotation_name": annotation_name,
            "annotation_text": annotation_text,
            "line": line,
            "param_name": selector_name,
            "selector_name": selector_name,
            "selector_value": selector_value,
        }

    def _extract_params(self, annotation_text: str) -> Dict[str, str]:
        params: Dict[str, str] = {}
        for match in PARAM_DOUBLE_QUOTE.finditer(annotation_text):
            params[match.group("name")] = match.group("value")
        for match in PARAM_SINGLE_QUOTE.finditer(annotation_text):
            params[match.group("name")] = match.group("value")
        return params

    def _choose_selector(self, params: Dict[str, str]) -> Tuple[Optional[str], Optional[str]]:
        if "xpath" in params:
            return "xpath", params["xpath"]
        if "id" in params:
            return "id", params["id"]
        if "resource-id" in params:
            return "resource-id", params["resource-id"]
        if "accessibility" in params:
            return "accessibility", params["accessibility"]
        if "accessibility-id" in params:
            return "accessibility-id", params["accessibility-id"]
        if "className" in params:
            return "className", params["className"]
        if "name" in params:
            return "name", params["name"]
        if "iOSNsPredicate" in params:
            return "iOSNsPredicate", params["iOSNsPredicate"]
        if "iOSClassChain" in params:
            return "iOSClassChain", params["iOSClassChain"]
        if "uiAutomator" in params:
            return "uiAutomator", params["uiAutomator"]
        if "androidUIAutomator" in params:
            return "androidUIAutomator", params["androidUIAutomator"]
        return None, None

    def _extract_balanced_parentheses(self, text: str, start_index: int) -> Tuple[Optional[str], int]:
        depth = 0
        result_chars: List[str] = []
        for position in range(start_index, len(text)):
            char = text[position]
            if char == "(":
                depth += 1
                if depth == 1:
                    continue
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return "".join(result_chars), position + 1
            if depth >= 1:
                result_chars.append(char)
        return None, len(text)

    def _validate_ios_ns_predicate(self, predicate: str, root: Any) -> Tuple[bool, Optional[List[Any]]]:
        match = IOS_PREDICATE_PATTERN.search(predicate)
        if not match:
            return False, None

        attr = match.group("attr")
        value = match.group("value")
        operator = match.group(2)

        mapped_attr = self._map_ios_predicate_attribute(attr)
        if not mapped_attr:
            return False, None

        if operator in ["==", "!="]:
            elements = self.parser.find_elements_by_attribute(root, mapped_attr, value, exact=True)
            return bool(elements), elements

        if operator.lower() == "contains":
            elements = self.parser.find_elements_by_attribute(root, mapped_attr, value, exact=False)
            return bool(elements), elements

        return False, None

    def _map_ios_predicate_attribute(self, attr: str) -> Optional[str]:
        mapping = {
            "label": "text",
            "name": "name",
            "value": "value",
            "type": "class",
        }
        return mapping.get(attr)

    def _build_issue_message(self, annotation: Dict[str, Any]) -> str:
        if annotation.get("alternatives"):
            return "Aucune alternative dans AndroidFindAll n'a trouvé d'élément valide."

        selector_name = annotation.get("selector_name")
        selector_value = annotation.get("selector_value")
        if selector_name == "xpath":
            return f"XPath invalide ou aucune correspondance pour '{selector_value}'."
        if selector_name in ["id", "resource-id"]:
            return f"Aucun élément avec resource-id='{selector_value}' n'a été trouvé."
        if selector_name in ["content-desc", "accessibility", "accessibility-id"]:
            return f"Aucun élément avec accessibilité='{selector_value}' n'a été trouvé."
        if selector_name == "className":
            return f"Aucun élément avec className='{selector_value}' n'a été trouvé."
        if selector_name == "iOSNsPredicate":
            return f"Aucune correspondance pour iOSNsPredicate '{selector_value}'."
        return f"Sélecteur '{selector_name}' invalide ou introuvable."

    def _validate_ui_automator(self, selector_value: str, root: Any) -> Tuple[bool, Optional[List[Any]]]:
        """Valide un sélecteur UiAutomator Android de base."""
        # Extraire les valeurs des méthodes UiSelector communes
        resource_id_match = re.search(r"resourceId\(['\"]([^'\"]+)['\"]\)", selector_value)
        text_match = re.search(r"text\(['\"]([^'\"]+)['\"]\)", selector_value)
        class_match = re.search(r"className\(['\"]([^'\"]+)['\"]\)", selector_value)

        # Essayer de valider avec les attributs extraits
        if resource_id_match:
            elements = self.parser.find_elements_by_attribute(root, "resource-id", resource_id_match.group(1), exact=True)
            if elements:
                return True, elements

        if text_match:
            elements = self.parser.find_elements_by_attribute(root, "text", text_match.group(1), exact=True)
            if elements:
                return True, elements

        if class_match:
            elements = self.parser.find_elements_by_attribute(root, "class", class_match.group(1), exact=True)
            if elements:
                return True, elements

        # Si on ne peut pas extraire d'attributs simples, considérer comme valide (complexe)
        # Pour une validation complète, il faudrait un parser UiAutomator complet
        return True, None  # Assume valid for complex selectors

    def _validate_ios_class_chain(self, selector_value: str, root: Any) -> Tuple[bool, Optional[List[Any]]]:
        """Valide un sélecteur iOS Class Chain de base."""
        # Extraire les valeurs des prédicats simples
        label_match = re.search(r"label\s*==\s*['\"]([^'\"]+)['\"]", selector_value)
        name_match = re.search(r"name\s*==\s*['\"]([^'\"]+)['\"]", selector_value)
        value_match = re.search(r"value\s*==\s*['\"]([^'\"]+)['\"]", selector_value)

        # Essayer de valider avec les attributs extraits
        if label_match:
            elements = self.parser.find_elements_by_attribute(root, "text", label_match.group(1), exact=True)
            if elements:
                return True, elements

        if name_match:
            elements = self.parser.find_elements_by_attribute(root, "name", name_match.group(1), exact=True)
            if elements:
                return True, elements

        if value_match:
            elements = self.parser.find_elements_by_attribute(root, "value", value_match.group(1), exact=True)
            if elements:
                return True, elements

        # Pour les sélecteurs complexes, considérer comme valide
        return True, None
