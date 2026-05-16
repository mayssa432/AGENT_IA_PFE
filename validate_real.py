#!/usr/bin/env python
from dom_inspector.dom_inspector import DomInspector

inspector = DomInspector()
snapshot = inspector.load_snapshot('auth_snapshot')
root = inspector.parse_snapshot(snapshot.xml)
issues = inspector.validate_page_object('AGENT_IA_PFE/src/test/java/com/orange/otvp/automation/pages/mobile/AuthenticationPO.java', root)
print('Issues with real DOM:', len(issues))
report = inspector.generate_validation_report('AGENT_IA_PFE/src/test/java/com/orange/otvp/automation/pages/mobile/AuthenticationPO.java', root)
report_path = inspector.save_validation_report(report, 'validation_AuthPO_real')
print('Report saved:', report_path)