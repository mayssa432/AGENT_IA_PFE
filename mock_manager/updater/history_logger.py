from datetime import datetime
import json
import os

LOG_FILE = os.path.join(
    os.getenv("OUTPUT_DIR", "./output"),
    "mock_history.json"
)

def log_update(
    url: str,
    method: str,
    mock_id: str,
    old_body: dict,
    new_body: dict,
    status_changed: bool
):
    """Log la mise à jour d'un mock dans un fichier JSON"""

    entry = {
        "timestamp": datetime.now().isoformat(),
        "url": url,
        "method": method,
        "mock_id": mock_id,
        "status_changed": status_changed,
        "old_body": old_body,
        "new_body": new_body
    }

    history = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                history = json.load(f)
            except:
                history = []

    history.append(entry)

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        json.dump(history, f, indent=2)

    print(f"📝 Log sauvegardé : {url} [{method}]")
