import requests
import os
from dotenv import load_dotenv

load_dotenv()

WIREMOCK_URL = os.getenv("WIREMOCK_URL", "http://localhost:8081")

def get_all_mocks() -> list:
    """Récupère tous les mocks depuis WireMock"""
    try:
        response = requests.get(
            f"{WIREMOCK_URL}/__admin/mappings",
            timeout=5
        )
        if response.status_code == 200:
            return response.json().get("mappings", [])
        return []
    except Exception as e:
        print(f"❌ WireMock non accessible : {e}")
        return []

def find_mock_for_url(url: str, method: str) -> dict:
    """Trouve un mock existant pour une URL et méthode données"""
    mocks = get_all_mocks()
    for mock in mocks:
        request = mock.get("request", {})
        mock_url = request.get("url", "") or request.get("urlPattern", "")
        mock_method = request.get("method", "")

        if mock_url in url and mock_method.upper() == method.upper():
            return mock
    return None
