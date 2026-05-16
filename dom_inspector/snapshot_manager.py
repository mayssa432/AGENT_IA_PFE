import json
import os
from datetime import datetime
from typing import Dict, Optional

from .models.dom_snapshot import DomSnapshot


class SnapshotManager:
    """Gère les snapshots DOM et leurs métadonnées."""

    def __init__(self, base_dir: str = "dom_snapshots"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def save(self, xml: str, name: str, metadata: Optional[Dict[str, str]] = None) -> DomSnapshot:
        metadata = metadata or {}
        timestamp = datetime.utcnow()
        filename = f"{name}.xml"
        path = os.path.join(self.base_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(xml)

        metadata_path = os.path.join(self.base_dir, f"{name}.meta.json")
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump({
                "created_at": timestamp.isoformat() + "Z",
                "metadata": metadata
            }, f, ensure_ascii=False, indent=2)

        return DomSnapshot(path=path, created_at=timestamp, metadata=metadata, xml=xml)

    def load(self, name: str) -> DomSnapshot:
        xml_path = os.path.join(self.base_dir, f"{name}.xml")
        metadata_path = os.path.join(self.base_dir, f"{name}.meta.json")

        if not os.path.exists(xml_path):
            raise FileNotFoundError(f"Snapshot introuvable : {xml_path}")

        with open(xml_path, "r", encoding="utf-8") as f:
            xml = f.read()

        metadata = {}
        created_at = datetime.utcfromtimestamp(os.path.getmtime(xml_path))
        if os.path.exists(metadata_path):
            with open(metadata_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                metadata = data.get("metadata", {})
                created_at = datetime.fromisoformat(data.get("created_at").replace("Z", "+00:00"))

        return DomSnapshot(path=xml_path, created_at=created_at, metadata=metadata, xml=xml)

    def list_snapshots(self) -> Dict[str, Dict[str, str]]:
        snapshots = {}
        for filename in os.listdir(self.base_dir):
            if filename.endswith(".xml"):
                name = filename[:-4]
                snapshots[name] = {
                    "xml": os.path.join(self.base_dir, filename),
                    "metadata": os.path.join(self.base_dir, f"{name}.meta.json")
                }
        return snapshots
