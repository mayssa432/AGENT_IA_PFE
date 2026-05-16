from lxml import etree
from typing import List, Dict, Optional


class UiParser:
    """Analyse le XML de DOM mobile et expose des helpers de recherche."""

    def parse_xml(self, xml: str) -> etree._Element:
        parser = etree.XMLParser(recover=True, remove_blank_text=True)
        return etree.fromstring(xml.encode("utf-8"), parser=parser)

    def element_to_dict(self, element: etree._Element) -> Dict[str, str]:
        data = {k: v for k, v in element.attrib.items()}
        data["tag"] = element.tag
        data["text"] = element.text or ""
        return data

    def find_elements_by_attribute(
        self,
        root: etree._Element,
        attribute: str,
        value: str,
        exact: bool = True
    ) -> List[etree._Element]:
        if exact:
            if "'" in value:
                xpath = f'//*[@{attribute}="{value}"]'
            else:
                xpath = f"//*[@{attribute}='{value}']"
        else:
            if "'" in value:
                xpath = f'//*[contains(@{attribute}, "{value}")]'
            else:
                xpath = f"//*[contains(@{attribute}, '{value}')]"
        return root.xpath(xpath)

    def find_elements_by_tag(self, root: etree._Element, tag: str) -> List[etree._Element]:
        return root.xpath(f"//{tag}")

    def get_element_path(self, element: etree._Element) -> str:
        tree = element.getroottree()
        return tree.getpath(element)

    def build_tree(self, element: etree._Element, depth: int = 0) -> Dict:
        node = self.element_to_dict(element)
        node["children"] = [self.build_tree(child, depth + 1) for child in element]
        return node
