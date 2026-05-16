from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class UiElement:
    tag: str
    text: str
    attributes: Dict[str, str]
    xpath: str
    depth: int = 0
    parent_xpath: Optional[str] = None

    def friendly_name(self) -> str:
        if self.attributes.get("resource-id"):
            return self.attributes["resource-id"]
        if self.attributes.get("content-desc"):
            return self.attributes["content-desc"]
        if self.text:
            return self.text.strip()
        return self.tag
