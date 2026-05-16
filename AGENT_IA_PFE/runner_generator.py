# -*- coding: utf-8 -*-
import os
from pathlib import Path

RUNNERS_DIR = r"C:\Users\m.derwich\Downloads\AGENT_IA_PFE\AGENT_IA_PFE\output\runners"
FEATURES_DIR = "src/test/resources/features"
STEPS_PACKAGE = "com.orange.otvp.automation.steps"

RUNNER_TEMPLATE = """package com.orange.otvp.automation.runners;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
    features = "{features_path}",
    glue = "{steps_package}",
    plugin = {{
        "pretty",
        "html:target/cucumber-reports/{page_name}-report.html",
        "json:target/cucumber-reports/{page_name}-report.json"
    }},
    monochrome = true
)
public class {page_name}Runner {{
}}
"""

def generate_runners():
    Path(RUNNERS_DIR).mkdir(parents=True, exist_ok=True)

    features_path = Path(
        r"C:\Users\m.derwich\Downloads\AGENT_IA_PFE\AGENT_IA_PFE\output\features"
    )
    feature_files = list(features_path.glob("*.feature"))

    print(f"\n[INFO] {len(feature_files)} runners à générer\n")

    success = 0
    for feature_file in feature_files:
        page_name = feature_file.stem
        feature_rel_path = f"{FEATURES_DIR}/{feature_file.name}"

        runner_content = RUNNER_TEMPLATE.format(
            features_path=feature_rel_path,
            steps_package=STEPS_PACKAGE,
            page_name=page_name
        )

        output_file = Path(RUNNERS_DIR) / f"{page_name}Runner.java"
        output_file.write_text(runner_content, encoding="utf-8")
        print(f"  [OK] {page_name}Runner.java")
        success += 1

    print(f"\n{'='*50}")
    print(f"[RÉSUMÉ] {success} runners générés")
    print(f"[OUTPUT] {RUNNERS_DIR}")
    print(f"{'='*50}")

if __name__ == "__main__":
    generate_runners()
