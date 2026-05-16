import difflib
import re
from typing import Any, Dict, List, Optional
from lxml.etree import XPathEvalError

from .ui_parser import UiParser

ATTR_REGEX = re.compile(r"@(?P<name>[\w-]+)\s*=\s*'(?P<value>[^']*)'")


class SelectorSuggester:
    """Suggère des sélecteurs robustes à partir d'un élément DOM."""

    def __init__(self):
        self.parser = UiParser()

    def suggest_for_annotation(
        self,
        annotation: Dict[str, Any],
        root: Any,
    ) -> Optional[Dict[str, str]]:
        selector_type = annotation["selector_name"]
        selector_value = annotation["selector_value"]

        if selector_type == "xpath":
            element = self._find_element_from_xpath(selector_value, root)
            if element is None:
                element = self._find_element_from_xpath_attributes(selector_value, root)
            if element is None:
                return None
            if isinstance(element, list):
                if not element:
                    return None
                element = element[0]
            return self._build_best_selector(element, annotation["annotation_name"])

        if selector_type in ["resource-id", "id", "content-desc", "accessibility", "name"]:
            element = self._find_element_by_attribute(selector_type, selector_value, root)
            if element is None:
                return None
            if isinstance(element, list):
                if not element:
                    return None
                element = element[0]
            return self._build_best_selector(element, annotation["annotation_name"])

        return None

    def _find_element_from_xpath(self, xpath: str, root: Any) -> Optional[Any]:
        try:
            elements = root.xpath(xpath)
            if isinstance(elements, list):
                return elements[0] if elements else None
            return elements
        except XPathEvalError:
            return None
        except Exception:
            return None
        return None

    def _find_element_from_xpath_attributes(self, xpath: str, root: Any) -> Optional[Any]:
        attrs = ATTR_REGEX.findall(xpath)
        for name, value in attrs:
            element = self._find_element_by_attribute(name, value, root)
            if element is not None:
                return element
        return None

    def _find_element_by_attribute(self, selector_type: str, selector_value: str, root: Any) -> Optional[Any]:
        if selector_type in ["resource-id", "id"]:
            elements = self.parser.find_elements_by_attribute(root, "resource-id", selector_value, exact=True)
            attribute = "resource-id"
        elif selector_type in ["content-desc", "accessibility"]:
            elements = self.parser.find_elements_by_attribute(root, "content-desc", selector_value, exact=True)
            attribute = "content-desc"
        elif selector_type == "name":
            elements = self.parser.find_elements_by_attribute(root, "name", selector_value, exact=True)
            attribute = "name"
        else:
            elements = []
            attribute = None

        if elements:
            return elements[0]

        if not attribute:
            return None

        candidate_elements = root.xpath(f'//*[@{attribute}]')
        candidate_values = [element.attrib.get(attribute, "") for element in candidate_elements if element.attrib.get(attribute)]
        best_matches = difflib.get_close_matches(selector_value, candidate_values, n=1, cutoff=0.5)
        if best_matches:
            best_value = best_matches[0]
            for element in candidate_elements:
                if element.attrib.get(attribute) == best_value:
                    return element

        normalized_value = selector_value.split("/")[-1]
        if normalized_value:
            for element in candidate_elements:
                attr_value = element.attrib.get(attribute, "")
                if normalized_value in attr_value:
                    return element

        return None

    def _build_best_selector(self, element: Any, annotation_name: str) -> Dict[str, str]:
        if isinstance(element, list):
            if not element:
                return {}
            element = element[0]
        attrs = {k: v for k, v in element.attrib.items()}
        suggestions: Dict[str, str] = {}

        # Primary selectors
        if attrs.get("resource-id"):
            suggestions["resource-id"] = attrs["resource-id"]
        if attrs.get("content-desc"):
            suggestions["content-desc"] = attrs["content-desc"]
        if attrs.get("accessibility-id"):
            suggestions["accessibility"] = attrs["accessibility-id"]

        # Generate Android UiAutomator selector
        ui_automator = self._generate_ui_automator(element)
        if ui_automator:
            suggestions["uiAutomator"] = ui_automator

        # Generate iOS Class Chain selector
        ios_class_chain = self._generate_ios_class_chain(element)
        if ios_class_chain:
            suggestions["iOSClassChain"] = ios_class_chain

        # Generate robust xpath with multiple attributes
        robust_xpath = self._generate_robust_xpath(element)
        if robust_xpath:
            suggestions["xpath"] = robust_xpath

        # Fallback xpath
        if not suggestions.get("xpath"):
            suggestions["xpath"] = self.parser.get_element_path(element)

        return self._prioritize_selector(suggestions, annotation_name)

    def _prioritize_selector(self, suggestions: Dict[str, str], annotation_name: str) -> Dict[str, str]:
        # Prioritize based on reliability and annotation type
        if annotation_name.startswith("Android"):
            priority_order = ["resource-id", "content-desc", "uiAutomator", "xpath"]
        elif annotation_name.startswith("iOS"):
            priority_order = ["accessibility", "name", "iOSClassChain", "xpath"]
        else:
            priority_order = ["resource-id", "content-desc", "accessibility", "uiAutomator", "iOSClassChain", "xpath"]

        for key in priority_order:
            if key in suggestions:
                return self._map_annotation_key({key: suggestions[key]}, annotation_name)

        # Fallback
        if suggestions:
            key = next(iter(suggestions))
            return self._map_annotation_key({key: suggestions[key]}, annotation_name)

        return {}

    def _map_annotation_key(self, selector: Dict[str, str], annotation_name: str) -> Dict[str, str]:
        src, value = next(iter(selector.items()))
        target_key = src

        if annotation_name == "FindBy":
            if src == "resource-id":
                target_key = "id"
            elif src in ["content-desc", "accessibility"]:
                target_key = "xpath"
        elif annotation_name in ["AndroidFindBy", "iOSXCUITFindBy"]:
            if src == "accessibility":
                target_key = "accessibility"
            elif src == "uiAutomator":
                target_key = "uiAutomator"
            elif src == "iOSClassChain":
                target_key = "iOSClassChain"
        return {"param_name": target_key, "value": value}

    def _generate_robust_xpath(self, element: Any) -> Optional[str]:
        """Generate a robust XPath using multiple attributes for uniqueness."""
        attrs = {k: v for k, v in element.attrib.items() if v}

        # Try combinations of attributes for uniqueness
        candidates = []

        # Single attribute xpaths
        if attrs.get("resource-id"):
            candidates.append(f"//*[@resource-id='{attrs['resource-id']}']")
        if attrs.get("content-desc"):
            candidates.append(f"//*[@content-desc='{attrs['content-desc']}']")
        if attrs.get("text") and attrs.get("class"):
            candidates.append(f"//{element.tag}[@class='{attrs['class']}' and @text='{attrs['text']}']")
        elif attrs.get("class"):
            candidates.append(f"//{element.tag}[@class='{attrs['class']}']")

        # Multi-attribute xpaths for better specificity
        if attrs.get("class") and attrs.get("resource-id"):
            candidates.append(f"//{element.tag}[@class='{attrs['class']}' and @resource-id='{attrs['resource-id']}']")
        if attrs.get("class") and attrs.get("content-desc"):
            candidates.append(f"//{element.tag}[@class='{attrs['class']}' and @content-desc='{attrs['content-desc']}']")

        # Find the most specific (shortest) xpath that uniquely identifies the element
        for xpath in candidates:
            try:
                matches = element.getroottree().xpath(xpath)
                if len(matches) == 1 and matches[0] == element:
                    return xpath
            except:
                continue

        return None

    def _generate_ui_automator(self, element: Any) -> Optional[str]:
        """Generate Android UiAutomator selector."""
        attrs = {k: v for k, v in element.attrib.items() if v}

        selectors = []
        if attrs.get("resource-id"):
            selectors.append(f"resourceId(\"{attrs['resource-id']}\")")
        if attrs.get("text"):
            selectors.append(f"text(\"{attrs['text']}\")")
        if attrs.get("class"):
            selectors.append(f"className(\"{attrs['class']}\")")

        if selectors:
            return f"new UiSelector().{'.'.join(selectors)}"

        return None

    def _generate_ios_class_chain(self, element: Any) -> Optional[str]:
        """Generate iOS Class Chain selector."""
        attrs = {k: v for k, v in element.attrib.items() if v}

        # Get element type from class or tag
        element_type = attrs.get("class", element.tag)
        if element_type and element_type.startswith("XCUIElementType"):
            type_short = element_type.replace("XCUIElementType", "")
        else:
            type_short = "Any"

        predicates = []
        if attrs.get("text"):
            predicates.append(f"label == \"{attrs['text']}\"")
        if attrs.get("name"):
            predicates.append(f"name == \"{attrs['name']}\"")
        if attrs.get("value"):
            predicates.append(f"value == \"{attrs['value']}\"")

        if predicates:
            predicate_str = " AND ".join(predicates)
            return f"**/XCUIElementType{type_short}[`${predicate_str}`]"

        return f"**/XCUIElementType{type_short}"
