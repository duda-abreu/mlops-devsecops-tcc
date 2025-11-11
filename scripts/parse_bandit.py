import json
import sys

with open(sys.argv[1]) as f:
    report = json.load(f)

results = report.get("results", [])
severity_count = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}

for r in results:
    sev = r.get("issue_severity", "").upper()
    if sev in severity_count:
        severity_count[sev] += 1

print("Resumo Bandit - Severidades:")
for sev, count in severity_count.items():
    print(f"{sev}: {count}")
