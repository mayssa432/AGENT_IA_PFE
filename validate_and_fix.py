#!/usr/bin/env python
"""
Script pour valider un Page Object Java contre un DOM,
corriger ses sélecteurs invalides,
et générer un rapport JSON détaillé.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Add workspace to sys.path
workspace_root = Path(__file__).parent
sys.path.insert(0, str(workspace_root))

from dom_inspector.dom_inspector import DomInspector


def main():
    java_file = workspace_root / 'dom_inspector' / 'CrashDialogPO.java'
    dom_file = workspace_root / 'dom_snapshots' / 'test_orange_otv.xml'
    report_dir = workspace_root / 'dom_reports'
    report_dir.mkdir(parents=True, exist_ok=True)
    
    # Create test Java file
    java_source = '''package dom_inspector;

import io.appium.java_client.pagefactory.AndroidFindBy;
import org.openqa.selenium.WebElement;

public class CrashDialogPO {
    @AndroidFindBy(id = "android:id/alertTtle")
    private WebElement title;

    @AndroidFindBy(id = "android:id/aerr_clos")
    private WebElement closeButton;

    @AndroidFindBy(xpath = "//android.widget.Button[@resource-id='android:id/aerr_waait']")
    private WebElement waitButton;
}
'''
    java_file.write_text(java_source, encoding='utf-8')
    print(f"✓ Fichier Java créé: {java_file}")
    
    # Initialize inspector
    inspector = DomInspector()
    dom_xml = dom_file.read_text(encoding='utf-8')
    root = inspector.parse_snapshot(dom_xml)
    print(f"✓ DOM chargé: {len(root.xpath('//*'))} éléments")
    
    # Step 1: Validate
    print("\n=== Étape 1: Validation ===")
    issues = inspector.validate_page_object(str(java_file), root)
    print(f"Sélecteurs invalides trouvés: {len(issues)}")
    for issue in issues:
        print(f"  Ligne {issue['line']}: {issue['selector_value']} - {issue['message']}")
    
    # Step 2: Fix (with error handling)
    print("\n=== Étape 2: Correction automatique ===")
    try:
        fix_result = inspector.fix_page_object(str(java_file), root)
        print(f"Rés ultat: {fix_result.get('success')}")
        print(f"Corrections appliquées: {fix_result.get('corrections_count')}")
        if fix_result.get('corrections'):
            for correction in fix_result['corrections']:
                print(f"  Ligne {correction['line']}: {correction['original']} -> {correction['fixed']}")
    except Exception as exc:
        print(f"Note: Correction partielle échouée: {exc}")
        fix_result = {
            'success': False,
            'error': str(exc),
            'corrections_count': 0,
            'corrections': []
        }
    
    # Step 3: Generate report
    print("\n=== Étape 3: Génération du rapport JSON ===")
    report = inspector.generate_validation_report(str(java_file), root)
    report['issues'] = issues
    report['fix'] = fix_result
    report['validated_at'] = datetime.utcnow().isoformat() + 'Z'
    
    report_path = report_dir / 'crash_dialog_validation_report.json'
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"✓ Rapport sauvegardé: {report_path}")
    
    print("\n=== Résumé ===")
    print(f"Fichier Java validé: {java_file.name}")
    print(f"Sélecteurs validés: {len([i for i in issues if i['valid']])}")
    print(f"Sélecteurs invalides: {len([i for i in issues if not i['valid']])}")
    print(f"Corrections appliquées: {fix_result.get('corrections_count', 0)}")
    print(f"Rapport: {report_path.name}")


if __name__ == '__main__':
    main()
