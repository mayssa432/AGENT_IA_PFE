from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional


@dataclass
class DomSnapshot:
    path: str
    created_at: datetime
    metadata: Dict[str, str]
    xml: str

    def summary(self) -> str:
        return (
            f"Snapshot saved at {self.created_at.isoformat()}\n"
            f"Path: {self.path}\n"
            f"Metadata: {self.metadata}"
        )
