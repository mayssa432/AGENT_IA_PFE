from fastapi import FastAPI
from dotenv import load_dotenv
from mock_manager.comparator.mock_loader import find_mock_for_url
from mock_manager.comparator.response_comparator import compare_responses
from mock_manager.comparator.diff_reporter import generate_diff_report
from mock_manager.updater.mock_updater import update_mock, create_new_mock
from mock_manager.updater.history_logger import log_update
from mock_manager.ai.llm_analyzer import analyze_diff_with_ai
import json
import os

load_dotenv()

app = FastAPI(title="Mock Manager API")
CAPTURE_DIR = "captured_responses"

@app.get("/health")
def health():
    return {"status": "✅ Mock Manager running"}

@app.post("/run")
def run_mock_manager():
    """Lance le Mock Manager complet"""
    print("\n🚀 Starting Mock Manager...\n")
    comparisons = []

    if not os.path.exists(CAPTURE_DIR):
        return {"message": "Aucune réponse capturée trouvée"}

    for filename in os.listdir(CAPTURE_DIR):
        if not filename.endswith(".json"):
            continue

        with open(f"{CAPTURE_DIR}/{filename}") as f:
            real_response = json.load(f)

        url = real_response.get("url")
        method = real_response.get("method")
        existing_mock = find_mock_for_url(url, method)

        if existing_mock:
            diff = compare_responses(real_response, existing_mock)
            comparisons.append(diff)

            if diff.has_differences:
                # 🤖 Analyse IA
                ai_analysis = analyze_diff_with_ai(
                    url=url,
                    method=method,
                    diff=diff.body_diff
                )
                print(f"🤖 AI: {ai_analysis}")

                if ai_analysis.get("should_update", True):
                    mock_id = existing_mock.get("id")
                    success = update_mock(mock_id, real_response)

                    if success:
                        log_update(
                            url=url,
                            method=method,
                            mock_id=mock_id,
                            old_body=existing_mock.get(
                                "response", {}
                            ).get("jsonBody", {}),
                            new_body=real_response.get(
                                "response_body", {}
                            ),
                            status_changed=diff.status_mismatch
                        )
        else:
            create_new_mock(real_response)

    return generate_diff_report(comparisons)

@app.get("/history")
def get_history():
    """Retourne l'historique des mises à jour"""
    log_file = os.path.join(
        os.getenv("OUTPUT_DIR", "./output"),
        "mock_history.json"
    )
    if os.path.exists(log_file):
        with open(log_file) as f:
            return json.load(f)
    return []
