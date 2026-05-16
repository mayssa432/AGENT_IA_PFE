from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class CapturedResponse(BaseModel):
    url: str
    method: str
    status_code: int
    request_headers: Optional[Dict[str, str]] = {}
    response_headers: Optional[Dict[str, str]] = {}
    response_body: Optional[Any] = None
    captured_at: Optional[str] = None

class MockResponse(BaseModel):
    id: Optional[str] = None
    url: str
    method: str
    status_code: int
    body: Optional[Any] = None

class DiffResult(BaseModel):
    url: str
    method: str
    has_differences: bool
    status_mismatch: bool
    body_diff: Optional[Dict[str, Any]] = {}
    mock_id: Optional[str] = None

class UpdateLog(BaseModel):
    url: str
    method: str
    mock_id: str
    old_body: Optional[Any] = None
    new_body: Optional[Any] = None
    status_changed: bool
    updated_at: str
