import os
from appium import webdriver
from typing import Dict, Optional


class AppiumConnector:
    """Connexion Appium et création de driver mobile."""

    def __init__(self, server_url: str = None):
        self.server_url = server_url or os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

    def create_driver(self, capabilities: Dict[str, str], timeout: int = 30) -> webdriver.Remote:
        """Crée un driver Appium pour l'appareil et l'application spécifiés."""
        if not capabilities:
            raise ValueError("Les capabilities Appium ne doivent pas être vides")

        from appium.options.android import UiAutomator2Options

        options = UiAutomator2Options()
        for key, value in capabilities.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor=self.server_url,
            options=options
        )
        driver.implicitly_wait(timeout)
        return driver

    def close_driver(self, driver: webdriver.Remote) -> None:
        try:
            driver.quit()
        except Exception:
            pass
