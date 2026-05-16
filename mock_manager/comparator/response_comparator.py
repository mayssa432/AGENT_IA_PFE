from deepdiff import DeepDiff
from mock_manager.models.schemas import DiffResult
import json

def compare_responses(
    real_response: dict,
    existing_mock: dict
) -> DiffResult:
    """
    Compare la vraie réponse API avec le mock existant
    """
    real_status = real_response.get("status_code", 200)
    mock_status = existing_mock.get(
        "response", {}
    ).get("status", 200)

    real_body = real_response.get("response_body", {})
    mock_body = existing_mock.get(
        "response", {}
    ).get("jsonBody", {})

    # Comparer les bodies
    try:
        diff = DeepDiff(mock_body, real_body, ignore_order=True)
        body_diff = diff.to_dict() if diff else {}
    except Exception:
        body_diff = {}

    has_differences = bool(body_diff) or (real_status != mock_status)

    return DiffResult(
        url=real_response.get("url", ""),
        method=real_response.get("method", ""),
        has_differences=has_differences,
        status_mismatch=(real_status != mock_status),
        body_diff=body_diff,
        mock_id=existing_mock.get("id")
    )
