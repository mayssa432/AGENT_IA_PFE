import json
import os
from datetime import datetime
from typing import Any, Dict, Optional


class ValidationReportManager:
    """Gère la sauvegarde des rapports de validation DOM."""

    def __init__(self, output_dir: str = "dom_reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_report(self, report: Dict[str, Any], report_name: Optional[str] = None) -> str:
        if not report_name:
            report_name = f"validation_report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        elif not report_name.endswith(".json"):
            report_name = f"{report_name}.json"

        path = os.path.join(self.output_dir, report_name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        return path
