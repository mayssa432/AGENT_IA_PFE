import os
from datetime import datetime
from typing import Any, Dict, List, Optional

from dom_inspector.appium_connector import AppiumConnector
from dom_inspector.dom_capture import DomCapture
from dom_inspector.report_manager import ValidationReportManager
from dom_inspector.selector_fixer import SelectorFixer
from dom_inspector.selector_validator import SelectorValidator
from dom_inspector.ui_parser import UiParser
from dom_inspector.snapshot_manager import SnapshotManager
from dom_inspector.models.ui_element import UiElement
from dom_inspector.models.dom_snapshot import DomSnapshot


class DomInspector:
    """Orchestre la capture et l'analyse du DOM mobile."""

    def __init__(self, appium_server_url: Optional[str] = None, output_dir: str = "dom_snapshots"):
        self.connector = AppiumConnector(server_url=appium_server_url)
        self.capture = DomCapture()
        self.parser = UiParser()
        self.snapshot_manager = SnapshotManager(output_dir)
        self.selector_validator = SelectorValidator()
        self.selector_fixer = SelectorFixer()
        self.report_manager = ValidationReportManager()

    def capture_dom(self, capabilities: Dict[str, str], snapshot_name: str = None) -> DomSnapshot:
        if not snapshot_name:
            snapshot_name = f"dom_snapshot_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"

        driver = self.connector.create_driver(capabilities)
        try:
            xml = self.capture.capture_page_source(driver)
            metadata = {
                "server_url": self.connector.server_url,
                "platformName": capabilities.get("platformName", "unknown"),
                "deviceName": capabilities.get("deviceName", "unknown"),
                "appPackage": capabilities.get("appPackage", "unknown"),
                "appActivity": capabilities.get("appActivity", "unknown"),
            }
            snapshot = self.snapshot_manager.save(xml, snapshot_name, metadata)
            return snapshot
        finally:
            self.connector.close_driver(driver)

    def load_snapshot(self, name: str) -> DomSnapshot:
        return self.snapshot_manager.load(name)

    def parse_snapshot(self, xml: str) -> any:
        return self.parser.parse_xml(xml)

    def find_elements_by_attribute(
        self,
        root: any,
        attribute: str,
        value: str,
        exact: bool = True
    ) -> List[UiElement]:
        elements = self.parser.find_elements_by_attribute(root, attribute, value, exact)
        return self._build_ui_elements(elements)

    def find_elements_by_text(self, root: any, text: str, exact: bool = False) -> List[UiElement]:
        if exact:
            xpath = f"//*[normalize-space(text())='{text}']"
        else:
            xpath = (
                f"//*[contains(normalize-space(text()), '{text}') "
                f"or contains(@content-desc, '{text}') "
                f"or contains(@resource-id, '{text}')]")
        elements = root.xpath(xpath)
        return self._build_ui_elements(elements)

    def suggest_selectors(self, element: any) -> Dict[str, str]:
        attributes = {k: v for k, v in element.attrib.items()}
        suggestions = {}

        if attributes.get("resource-id"):
            suggestions["resource-id"] = attributes["resource-id"]

        if attributes.get("content-desc"):
            suggestions["content-desc"] = attributes["content-desc"]

        if attributes.get("accessibility-id"):
            suggestions["accessibility-id"] = attributes["accessibility-id"]

        if attributes.get("class") and attributes.get("text"):
            suggestions["xpath"] = (
                f"//{element.tag}[@class='{attributes['class']}' and @text='{attributes['text']}']"
            )
        elif attributes.get("class"):
            suggestions["xpath"] = f"//{element.tag}[@class='{attributes['class']}']"
        else:
            suggestions["xpath"] = self.parser.get_element_path(element)

        return suggestions

    def _build_ui_elements(self, elements: List[any]) -> List[UiElement]:
        ui_elements = []
        for element in elements:
            xpath = self.parser.get_element_path(element)
            attributes = {k: v for k, v in element.attrib.items()}
            ui_elements.append(UiElement(
                tag=element.tag,
                text=(element.text or "").strip(),
                attributes=attributes,
                xpath=xpath,
                depth=len(xpath.split("/")) - 1,
                parent_xpath="/".join(xpath.split("/")[:-1]) if "/" in xpath else ""
            ))
        return ui_elements

    def validate_page_object(self, java_file: str, root: Any) -> List[Dict[str, Any]]:
        return self.selector_validator.validate_file(java_file, root)

    def fix_page_object(self, java_file: str, root: Any) -> Dict[str, Any]:
        return self.selector_fixer.fix_file(java_file, root)

    def generate_validation_report(self, java_file: str, root: Any, snapshot_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        issues = self.selector_validator.validate_file(java_file, root)
        return {
            "java_file": java_file,
            "snapshot_metadata": snapshot_metadata or {},
            "validated_at": datetime.utcnow().isoformat() + "Z",
            "issues_count": len(issues),
            "issues": issues,
        }

    def save_validation_report(self, report: Dict[str, Any], report_name: Optional[str] = None) -> str:
        return self.report_manager.save_report(report, report_name)
