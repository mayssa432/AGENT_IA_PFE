#!/usr/bin/env python
import os
import json
from datetime import datetime

# Load all batch reports
report_dir = 'dom_reports'
batch_reports = [f for f in os.listdir(report_dir) if f.startswith('batch_') and f.endswith('.json')]

summary = {
    'batch_validation_summary': {
        'total_files': len(batch_reports),
        'validated_at': datetime.utcnow().isoformat() + 'Z',
        'dom_snapshot': 'auth_snapshot.xml',
        'reports': []
    }
}

total_issues = 0
for report_file in batch_reports:
    with open(os.path.join(report_dir, report_file), 'r', encoding='utf-8') as f:
        report = json.load(f)
        summary['batch_validation_summary']['reports'].append({
            'file': report['java_file'],
            'issues_count': report['issues_count']
        })
        total_issues += report['issues_count']

summary['batch_validation_summary']['total_issues'] = total_issues
summary['batch_validation_summary']['average_issues_per_file'] = total_issues / len(batch_reports) if batch_reports else 0

# Save summary
with open('dom_reports/batch_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f'Batch summary saved: dom_reports/batch_summary.json')
print(f'Total files: {len(batch_reports)}')
print(f'Total issues: {total_issues}')
print(f'Average issues per file: {total_issues / len(batch_reports):.1f}')