import re
import os
from typing import Any, Dict, List, Optional

from .selector_validator import SelectorValidator
from .selector_suggester import SelectorSuggester

ANNOTATION_PARAM_PATTERN = re.compile(r'(\w+)\s*=\s*"((?:[^"\\]|\\.)*)"')


class SelectorFixer:
    """Corrige automatiquement les selecteurs d'un Page Object Java."""

    def __init__(self):
        self.validator = SelectorValidator()
        self.suggester = SelectorSuggester()

    def fix_file(self, file_path: str, root: Any) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            return {
                "success": False,
                "error": f"Fichier introuvable : {file_path}",
            }

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        annotations = self.validator.parse_annotations(file_path)
        corrections: List[Dict[str, Any]] = []
        fixed_lines = list(lines)

        for annotation in annotations:
            if annotation.get("alternatives"):
                # AndroidFindAll with multiple alternatives is validated as a group.
                valid = any(
                    self.validator.validate_selector(
                        alt["selector_name"],
                        alt["selector_value"],
                        root,
                    )[0]
                    for alt in annotation["alternatives"]
                )
                if valid:
                    continue
                # Auto-fixing AndroidFindAll candidate groups is not supported yet.
                continue

            valid, _ = self.validator.validate_selector(
                annotation["selector_name"],
                annotation["selector_value"],
                root,
            )
            if valid:
                continue

            suggestion = self.suggester.suggest_for_annotation(annotation, root)
            if not suggestion:
                continue

            line_index = annotation["line"] - 1
            original_line = fixed_lines[line_index]
            new_line = self._replace_selector_value(
                original_line,
                annotation["param_name"],
                annotation["selector_value"],
                suggestion["param_name"],
                suggestion["value"],
            )

            if original_line != new_line:
                corrections.append({
                    "line": annotation["line"],
                    "original": original_line.strip(),
                    "fixed": new_line.strip(),
                    "suggestion": suggestion,
                })
                fixed_lines[line_index] = new_line

        if not corrections:
            return {
                "success": True,
                "file": os.path.basename(file_path),
                "corrections_count": 0,
                "corrections": [],
            }

        backup_path = self._backup_file(file_path)
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(fixed_lines)

        return {
            "success": True,
            "file": os.path.basename(file_path),
            "backup": backup_path,
            "corrections_count": len(corrections),
            "corrections": corrections,
        }

    def _replace_selector_value(
        self,
        line: str,
        old_param: str,
        old_value: str,
        new_param: str,
        new_value: str,
    ) -> str:
        escaped_old = re.escape(old_param) + r"\s*=\s*\"" + re.escape(old_value) + r"\""
        replacement = f'{new_param} = "{new_value}"'
        new_line, count = re.subn(escaped_old, replacement, line, count=1)
        if count == 0 and old_param != new_param:
            # fallback: replace the old value only
            old_value_pattern = re.escape(old_value)
            new_line = re.sub(old_value_pattern, new_value, line, count=1)
        return new_line

    def _backup_file(self, file_path: str) -> str:
        backup_dir = os.path.join("backups", "selector_fixer")
        os.makedirs(backup_dir, exist_ok=True)
        backup_path = os.path.join(
            backup_dir,
            f"{os.path.basename(file_path)}.{os.path.getmtime(file_path):.0f}.bak",
        )
        with open(file_path, "r", encoding="utf-8") as source, open(backup_path, "w", encoding="utf-8") as dest:
            dest.writelines(source.readlines())
        return backup_path
