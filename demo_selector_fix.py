"""
demo_selector_fix.py — Démo de la boucle auto-correction sélecteurs (Livrable #2 PFE)

Ce script démontre de façon complète et reproductible la boucle :
  1. Chargement d'un DOM XML réel (snapshot ou mock)
  2. Injection d'un sélecteur cassé dans un Page Object Java (copie de test)
  3. Détection automatique via SelectorValidator
  4. Correction automatique via SelectorFixer
  5. Vérification que le nouveau sélecteur est valide dans le DOM
  6. Restauration du fichier original

Usage :
    venv\\Scripts\\python.exe demo_selector_fix.py
    venv\\Scripts\\python.exe demo_selector_fix.py --po-file path/to/YourPO.java --dom path/to/dom.xml
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Localiser le venv ou le chemin courant
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))

from dom_inspector.ui_parser import UiParser
from dom_inspector.selector_validator import SelectorValidator
from dom_inspector.selector_fixer import SelectorFixer
from dom_inspector.selector_suggester import SelectorSuggester

# ---------------------------------------------------------------------------
# DOM mock minimal — suffisant pour la démo sans device réel
# ---------------------------------------------------------------------------
MOCK_DOM = """<?xml version="1.0" encoding="UTF-8"?>
<hierarchy rotation="0">
  <android.widget.FrameLayout resource-id="com.orange.otvp:id/root_view" bounds="[0,0][1080,1920]">
    <android.widget.LinearLayout resource-id="com.orange.otvp:id/main_container">
      <android.widget.TextView
        resource-id="com.orange.otvp:id/live_channel_title"
        text="Orange TV"
        content-desc="live_channel_title_desc"
        bounds="[0,100][500,150]"/>
      <android.widget.Button
        resource-id="com.orange.otvp:id/btn_play"
        text="Lecture"
        content-desc="btn_play_desc"
        bounds="[0,200][300,250]"/>
      <android.widget.ImageView
        resource-id="com.orange.otvp:id/channel_logo"
        content-desc="channel_logo_desc"
        bounds="[0,300][100,400]"/>
      <android.widget.TextView
        resource-id="com.orange.otvp:id/program_title"
        text="Journal de 20h"
        content-desc="program_title_desc"
        bounds="[0,400][500,450]"/>
      <android.widget.Button
        resource-id="com.orange.otvp:id/btn_record"
        text="Enregistrer"
        content-desc="btn_record_desc"
        bounds="[0,500][300,550]"/>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>"""

# ---------------------------------------------------------------------------
# Page Object Java de démo avec un sélecteur intentionnellement cassé
# ---------------------------------------------------------------------------
DEMO_PO_BROKEN = """package com.orange.otvp.automation.pages.mobile;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import lombok.Getter;
import org.openqa.selenium.WebElement;

@Getter
public class LiveDemoPO {

    // ✅ Sélecteur VALIDE — sera détecté comme OK
    @AndroidFindBy(accessibility = "btn_play_desc")
    private WebElement playButton;

    // ❌ Sélecteur CASSÉ — resource-id inexistant dans le DOM
    @AndroidFindBy(xpath = "//*[@resource-id='com.orange.otvp:id/INEXISTANT_BROKEN_SELECTOR']")
    private WebElement brokenElement;

    // ❌ Sélecteur CASSÉ — XPath absolu fragile pointant nul part
    @AndroidFindBy(xpath = "/html/body/div[3]/span[2]/button")
    private WebElement absoluteXpathBroken;

    // ✅ Sélecteur VALIDE — sera détecté comme OK
    @AndroidFindBy(accessibility = "program_title_desc")
    private WebElement programTitle;

    public LiveDemoPO(AppiumDriver driver) {
        new org.openqa.selenium.support.PageFactory().initElements(
            new AppiumFieldDecorator(driver), this);
    }
}
"""

# ---------------------------------------------------------------------------
# Helpers console
# ---------------------------------------------------------------------------

def _sep(title: str = "") -> None:
    print(f"\n{'─' * 60}")
    if title:
        print(f"  {title}")
        print(f"{'─' * 60}")


def _ok(msg: str) -> None:
    print(f"  ✅  {msg}")


def _fail(msg: str) -> None:
    print(f"  ❌  {msg}")


def _info(msg: str) -> None:
    print(f"  ℹ️   {msg}")


# ---------------------------------------------------------------------------
# Pipeline de démo
# ---------------------------------------------------------------------------

def run_demo(po_file: str = None, dom_file: str = None) -> dict:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    print(f"\n{'═' * 60}")
    print(f"  🤖  DÉMO AUTO-CORRECTION SÉLECTEURS — PFE")
    print(f"  Run : {run_id}")
    print(f"{'═' * 60}")

    tmp_dir = tempfile.mkdtemp(prefix="pfe_demo_")
    results = {"run_id": run_id, "steps": []}

    try:
        # ------------------------------------------------------------------
        # ÉTAPE 1 — Charger le DOM (snapshot ou mock)
        # ------------------------------------------------------------------
        _sep("ÉTAPE 1 — Chargement du DOM")

        if dom_file and os.path.exists(dom_file):
            with open(dom_file, "r", encoding="utf-8") as f:
                dom_xml = f.read()
            _ok(f"DOM chargé depuis : {dom_file}")
        else:
            dom_xml = MOCK_DOM
            _ok("DOM mock embarqué utilisé (simule le page_source Appium).")

        parser = UiParser()
        root = parser.parse_xml(dom_xml)
        _ok(f"DOM parsé — tag racine : {root.tag}, {len(list(root.iter()))} noeuds")

        results["steps"].append({"step": 1, "status": "ok", "dom_nodes": len(list(root.iter()))})

        # ------------------------------------------------------------------
        # ÉTAPE 2 — Préparer un Page Object avec sélecteurs cassés
        # ------------------------------------------------------------------
        _sep("ÉTAPE 2 — Page Object avec sélecteurs cassés")

        if po_file and os.path.exists(po_file):
            test_po = os.path.join(tmp_dir, os.path.basename(po_file))
            shutil.copy2(po_file, test_po)
            _ok(f"PO copié depuis : {po_file}")
        else:
            test_po = os.path.join(tmp_dir, "LiveDemoPO.java")
            with open(test_po, "w", encoding="utf-8") as f:
                f.write(DEMO_PO_BROKEN)
            _ok("PO de démo avec 2 sélecteurs intentionnellement cassés créé.")

        _info(f"Fichier de test : {test_po}")

        results["steps"].append({"step": 2, "status": "ok", "po_file": test_po})

        # ------------------------------------------------------------------
        # ÉTAPE 3 — Détection des sélecteurs invalides
        # ------------------------------------------------------------------
        _sep("ÉTAPE 3 — Détection des sélecteurs cassés")

        validator = SelectorValidator()
        issues = validator.validate_file(test_po, root)

        if issues:
            _fail(f"{len(issues)} sélecteur(s) invalide(s) détecté(s) :")
            for issue in issues:
                print(f"       ligne {issue['line']:3d} │ {issue.get('selector_name','?')} = {str(issue.get('selector_value',''))[:60]}")
        else:
            _ok("Aucun sélecteur invalide (DOM très pauvre — tous non trouvés = neutre).")

        results["steps"].append({"step": 3, "status": "ok", "issues_count": len(issues), "issues": issues})

        # ------------------------------------------------------------------
        # ÉTAPE 4 — Correction automatique
        # ------------------------------------------------------------------
        _sep("ÉTAPE 4 — Correction automatique des sélecteurs")

        fixer = SelectorFixer()
        fix_result = fixer.fix_file(test_po, root)

        corrections = fix_result.get("corrections", [])
        if corrections:
            _ok(f"{len(corrections)} correction(s) appliquée(s) :")
            for c in corrections:
                print(f"       ligne {c['line']:3d} │ AVANT  : {c['original'][:70]}")
                print(f"              │ APRÈS  : {c['fixed'][:70]}")
                print()
        else:
            _info("Aucune correction automatique possible avec ce DOM.")
            _info("→ En prod, le DOM réel (Appium) contient les éléments cibles.")

        results["steps"].append({
            "step": 4,
            "status": "ok",
            "corrections_count": len(corrections),
            "corrections": corrections,
            "backup": fix_result.get("backup"),
        })

        # ------------------------------------------------------------------
        # ÉTAPE 5 — Validation post-correction
        # ------------------------------------------------------------------
        _sep("ÉTAPE 5 — Validation post-correction")

        if corrections:
            issues_after = validator.validate_file(test_po, root)
            broken_before = len(issues)
            broken_after = len(issues_after)
            fixed_count = broken_before - broken_after

            if fixed_count > 0:
                _ok(f"Sélecteurs cassés avant : {broken_before}  →  après : {broken_after}  "
                    f"(+{fixed_count} réparés ✅)")
            else:
                _info(f"Sélecteurs cassés : {broken_before} → {broken_after} (DOM mock trop pauvre pour valider).")

            results["steps"].append({
                "step": 5,
                "status": "ok",
                "broken_before": broken_before,
                "broken_after": broken_after,
                "repaired": fixed_count,
            })
        else:
            _info("Validation post-correction ignorée (aucune correction appliquée).")
            results["steps"].append({"step": 5, "status": "skipped"})

        # ------------------------------------------------------------------
        # ÉTAPE 6 — Afficher le diff du fichier corrigé
        # ------------------------------------------------------------------
        _sep("ÉTAPE 6 — Contenu final du Page Object corrigé")

        with open(test_po, "r", encoding="utf-8") as f:
            final_content = f.readlines()

        print("  --- Page Object après correction ---")
        for i, line in enumerate(final_content, 1):
            print(f"  {i:3d} │ {line}", end="")
        print()

        # ------------------------------------------------------------------
        # RÉSUMÉ
        # ------------------------------------------------------------------
        _sep()
        report_path = os.path.join("output", "reports", f"demo_fix_{run_id}.json")
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        results["summary"] = {
            "issues_detected": len(issues),
            "corrections_applied": len(corrections),
            "demo_po": test_po,
        }
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2, default=str)

        print(f"""
╔══════════════════════════════════════════╗
║  ✅  Démo Livrable #2 terminée           ║
║──────────────────────────────────────────║
║  Sélecteurs cassés détectés : {len(issues):<10} ║
║  Corrections appliquées     : {len(corrections):<10} ║
║  Rapport                    : output/reports/demo_fix_{run_id}.json
╚══════════════════════════════════════════╝
""")

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Démo boucle auto-correction sélecteurs — PFE Livrable #2"
    )
    parser.add_argument("--po-file", help="Chemin vers un Page Object Java réel à tester")
    parser.add_argument("--dom", help="Chemin vers un snapshot DOM XML (Appium page_source)")
    args = parser.parse_args()

    run_demo(po_file=args.po_file, dom_file=args.dom)


if __name__ == "__main__":
    main()
