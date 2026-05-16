from appium.webdriver.webdriver import WebDriver
from typing import Optional
import os


class DomCapture:
    """Capture et sauvegarde du DOM mobile via Appium."""

    def capture_page_source(self, driver: WebDriver) -> str:
        """Récupère la structure XML de l'écran actuel."""
        return driver.page_source

    def save_snapshot(self, xml: str, output_dir: str, filename: str = "dom_snapshot.xml") -> str:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(xml)
        return path

    def capture_and_save(self, driver: WebDriver, output_dir: str, filename: str = "dom_snapshot.xml") -> str:
        xml = self.capture_page_source(driver)
        return self.save_snapshot(xml, output_dir, filename)
