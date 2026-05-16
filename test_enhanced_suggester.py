#!/usr/bin/env python
from dom_inspector.dom_inspector import DomInspector

inspector = DomInspector()
xml = open('dom_snapshots/mock_auth_dom.xml', 'r', encoding='utf-8').read()
root = inspector.parse_snapshot(xml)
result = inspector.fix_page_object('AGENT_IA_PFE/src/test/java/com/orange/otvp/automation/pages/mobile/AuthenticationPO.java', root)
print('Fix result:', result)