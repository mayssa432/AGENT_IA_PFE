import re
from typing import List, Dict
from utils.file_utils import read_file, get_file_name


class GherkinScenario:
    """Représente un scénario Gherkin"""

    def __init__(self, title: str, steps: List[str], line: int):
        self.title = title
        self.steps = steps
        self.line = line

    def __repr__(self):
        return f"GherkinScenario(title={self.title}, steps={len(self.steps)})"


class GherkinParser:
    """Parse les fichiers .feature Gherkin"""

    SCENARIO_PATTERN = re.compile(
        r'^\s*(Scenario|Scenario Outline):\s*(.+)$',
        re.MULTILINE
    )
    STEP_PATTERN = re.compile(
        r'^\s*(Given|When|Then|And|But)\s+(.+)$',
        re.MULTILINE
    )
    FEATURE_PATTERN = re.compile(
        r'^\s*Feature:\s*(.+)$',
        re.MULTILINE
    )

    def parse(self, file_path: str) -> List[GherkinScenario]:
        """Parse un fichier .feature et retourne les scénarios"""
        content = read_file(file_path)
        scenarios = []

        # Trouver tous les scénarios
        scenario_matches = list(self.SCENARIO_PATTERN.finditer(content))

        for i, match in enumerate(scenario_matches):
            title = match.group(2).strip()
            line_num = content[:match.start()].count('\n') + 1

            # Extraire les steps jusqu'au prochain scénario
            start = match.end()
            end = (
                scenario_matches[i + 1].start()
                if i + 1 < len(scenario_matches)
                else len(content)
            )
            block = content[start:end]

            # Extraire les steps
            steps = []
            for step_match in self.STEP_PATTERN.finditer(block):
                keyword = step_match.group(1)
                step_text = step_match.group(2).strip()
                steps.append(f"{keyword} {step_text}")

            scenarios.append(GherkinScenario(
                title=title,
                steps=steps,
                line=line_num
            ))

        return scenarios

    def get_feature_name(self, file_path: str) -> str:
        """Retourne le nom de la feature"""
        content = read_file(file_path)
        match = self.FEATURE_PATTERN.search(content)
        return match.group(1).strip() if match else get_file_name(file_path)

    def detect_duplicate_scenarios(
        self,
        file_path: str
    ) -> List[Dict]:
        """Détecte les scénarios dupliqués dans un fichier feature"""
        scenarios = self.parse(file_path)
        duplicates = []
        seen_titles = {}

        for scenario in scenarios:
            title = scenario.title.lower().strip()
            if title in seen_titles:
                duplicates.append({
                    "title": scenario.title,
                    "line_first": seen_titles[title],
                    "line_duplicate": scenario.line
                })
            else:
                seen_titles[title] = scenario.line

        return duplicates

    def detect_missing_steps(
        self,
        file_path: str
    ) -> List[Dict]:
        """Détecte les scénarios sans steps"""
        scenarios = self.parse(file_path)
        missing = []

        for scenario in scenarios:
            if not scenario.steps:
                missing.append({
                    "title": scenario.title,
                    "line": scenario.line
                })

        return missing

    def get_stats(self, file_path: str) -> Dict:
        """Retourne les statistiques d'un fichier feature"""
        scenarios = self.parse(file_path)
        total_steps = sum(len(s.steps) for s in scenarios)

        return {
            "feature": self.get_feature_name(file_path),
            "file": get_file_name(file_path),
            "total_scenarios": len(scenarios),
            "total_steps": total_steps,
            "avg_steps": (
                round(total_steps / len(scenarios), 1)
                if scenarios else 0
            )
        }
