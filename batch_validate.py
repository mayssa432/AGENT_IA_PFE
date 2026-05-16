#!/usr/bin/env python
import os
from dom_inspector.dom_inspector import DomInspector

inspector = DomInspector()
snapshot = inspector.load_snapshot('auth_snapshot')
root = inspector.parse_snapshot(snapshot.xml)
mobile_dir = 'AGENT_IA_PFE/src/test/java/com/orange/otvp/automation/pages/mobile'
java_files = [f for f in os.listdir(mobile_dir) if f.endswith('.java')]
print(f'Found {len(java_files)} Java files')

results = {}
for java_file in java_files:
    full_path = os.path.join(mobile_dir, java_file)
    issues = inspector.validate_page_object(full_path, root)
    results[java_file] = len(issues)
    report = inspector.generate_validation_report(full_path, root)
    report_path = inspector.save_validation_report(report, f'batch_{java_file}')
    print(f'{java_file}: {len(issues)} issues')

print(f'Total validated: {len(results)} files')
print('Summary:', results)