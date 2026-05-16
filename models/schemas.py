from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class SeverityLevel(str, Enum):
    CRITICAL = "CRITICAL"
    IMPORTANT = "IMPORTANT"
    WARNING = "WARNING"
    INFO = "INFO"

class IssueType(str, Enum):
    DUPLICATE_FIELD = "DUPLICATE_FIELD"
    INVALID_ANNOTATION = "INVALID_ANNOTATION"
    INVALID_XPATH = "INVALID_XPATH"
    STATIC_FIELD = "STATIC_FIELD"
    INVALID_SELECTOR = "INVALID_SELECTOR"

class Issue(BaseModel):
    issue_type: IssueType
    severity: SeverityLevel
    file: str
    field: Optional[str] = None
    line: Optional[int] = None
    detail: str
    suggestion: Optional[str] = None

class FileReport(BaseModel):
    file_name: str
    file_path: str
    total_fields: int
    issues: List[Issue]
    is_valid: bool

class AnalysisReport(BaseModel):
    project_path: str
    total_files: int
    total_issues: int
    critical_count: int
    important_count: int
    warning_count: int
    files: List[FileReport]
    summary: str
