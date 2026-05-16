import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

WIREMOCK_URL = os.getenv("WIREMOCK_URL", "http://localhost:8081")

def update_mock(mock_id: str, real_response: dict) -> bool:
    """Met à jour un mock existant dans WireMock"""
    try:
        new_body = real_response.get("response_body", {})
        status_code = real_response.get("status_code", 200)
        url = real_response.get("url", "")
        method = real_response.get("method", "GET")

        payload = {
            "request": {
                "method": method.upper(),
                "url": url
            },
            "response": {
                "status": status_code,
                "jsonBody": new_body,
                "headers": {
                    "Content-Type": "application/json"
                }
            }
        }

        response = requests.put(
            f"{WIREMOCK_URL}/__admin/mappings/{mock_id}",
            json=payload,
            timeout=5
        )
        return response.status_code == 200

    except Exception as e:
        print(f"❌ Erreur mise à jour mock : {e}")
        return False

def create_new_mock(real_response: dict) -> bool:
    """Crée un nouveau mock dans WireMock"""
    try:
        payload = {
            "request": {
                "method": real_response.get("method", "GET").upper(),
                "url": real_response.get("url", "")
            },
            "response": {
                "status": real_response.get("status_code", 200),
                "jsonBody": real_response.get("response_body", {}),
                "headers": {
                    "Content-Type": "application/json"
                }
            }
        }

        response = requests.post(
            f"{WIREMOCK_URL}/__admin/mappings",
            json=payload,
            timeout=5
        )
        return response.status_code == 201

    except Exception as e:
        print(f"❌ Erreur création mock : {e}")
        return False
