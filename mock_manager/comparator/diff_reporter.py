from mock_manager.models.schemas import DiffResult
from typing import List
from datetime import datetime

def generate_diff_report(diffs: List[DiffResult]) -> dict:
    """Génère un rapport des différences détectées"""

    total = len(diffs)
    with_diff = [d for d in diffs if d.has_differences]
    without_diff = [d for d in diffs if not d.has_differences]

    return {
        "generated_at": datetime.now().isoformat(),
        "total_compared": total,
        "updated": len(with_diff),
        "unchanged": len(without_diff),
        "details": [
            {
                "url": d.url,
                "method": d.method,
                "has_differences": d.has_differences,
                "status_mismatch": d.status_mismatch,
                "mock_id": d.mock_id
            }
            for d in diffs
        ]
    }
