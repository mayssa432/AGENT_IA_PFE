#!/usr/bin/env python
"""
Generate a mock DOM XML that matches the selectors in AuthenticationPO.java
for demonstration purposes.
"""

import xml.etree.ElementTree as ET
from dom_inspector.selector_validator import SelectorValidator

def generate_mock_dom():
    validator = SelectorValidator()
    annotations = validator.parse_annotations('AGENT_IA_PFE/src/test/java/com/orange/otvp/automation/pages/mobile/AuthenticationPO.java')

    # Root element
    root = ET.Element("hierarchy", {"rotation": "0", "width": "1080", "height": "2400"})
    frame = ET.SubElement(root, "android.widget.FrameLayout", {
        "package": "com.orange.owtv.prod",
        "class": "android.widget.FrameLayout",
        "text": "",
        "resource-id": "android:id/content",
        "bounds": "[0,0][1080,2400]",
        "displayed": "true"
    })

    # Add elements for each selector
    for ann in annotations:
        if ann.get('alternatives'):
            for alt in ann['alternatives']:
                add_element_for_selector(frame, alt['selector_name'], alt['selector_value'])
        else:
            add_element_for_selector(frame, ann['selector_name'], ann['selector_value'])

    # Write to file
    tree = ET.ElementTree(root)
    tree.write('dom_snapshots/mock_auth_dom.xml', encoding='utf-8', xml_declaration=True)
    print("Mock DOM generated: dom_snapshots/mock_auth_dom.xml")

def add_element_for_selector(parent, selector_name, selector_value):
    if selector_name == 'id':
        ET.SubElement(parent, "android.widget.Button", {
            "resource-id": selector_value,
            "class": "android.widget.Button",
            "text": f"Button {selector_value}",
            "bounds": "[100,100][200,150]",
            "displayed": "true"
        })
    elif selector_name == 'accessibility':
        ET.SubElement(parent, "android.widget.TextView", {
            "content-desc": selector_value,
            "class": "android.widget.TextView",
            "text": f"Text {selector_value}",
            "bounds": "[100,100][200,150]",
            "displayed": "true"
        })
    elif selector_name == 'xpath':
        # For xpath like //*[@text='Sign-in'], add an element with text
        if "'Sign-in'" in selector_value:
            ET.SubElement(parent, "android.widget.TextView", {
                "text": "Sign-in",
                "class": "android.widget.TextView",
                "bounds": "[100,100][200,150]",
                "displayed": "true"
            })
        elif "'Identifiez-vous'" in selector_value:
            ET.SubElement(parent, "android.widget.TextView", {
                "text": "Identifiez-vous",
                "class": "android.widget.TextView",
                "bounds": "[100,100][200,150]",
                "displayed": "true"
            })
    # Skip iOS selectors for Android DOM

if __name__ == '__main__':
    generate_mock_dom()