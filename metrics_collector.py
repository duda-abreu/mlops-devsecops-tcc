import json
import os
import time

REPORT_DIR = "reports"

def read_bandit(path):
    if not os.path.exists(path):
        return 0
    with open(path, "r") as f:
        data = json.load(f)
    return len(data.get("results", []))

def read_safety(path):
    if not os.path.exists(path):
        return 0
    with open(path, "r") as f:
        data = json.load(f)
    return len(data.get("vulnerabilities", []))

def read_trivy(path):
    if not os.path.exists(path):
        return 0
    with open(path, "r") as f:
        data = json.load(f)
    vulnerabilities = 0
    for result in data.get("Results", []):
        vulnerabilities += len(result.get("Vulnerabilities", []))
    return vulnerabilities

def collect_metrics():
    metrics = {}

    metrics["bandit"] = read_bandit(os.path.join(REPORT_DIR, "bandit_report.json"))
    metrics["safety"] = read_safety(os.path.join(REPORT_DIR, "safety_report.json"))
    metrics["trivy"] = read_trivy(os.path.join(REPORT_DIR, "trivy_report.json"))

    return metrics

# Comparar baseline vs mlops
def compare_metrics(baseline_metrics, mlops_metrics):
    print("\n--- Comparação de métricas ---")
    for key in mlops_metrics:
        b_val = baseline_metrics.get(key, 0)
        m_val = mlops_metrics.get(key, 0)
        print(f"{key.capitalize()}: Baseline = {b_val}, MLOps = {m_val}")

if __name__ == "__main__":
    print("Coletando métricas baseline...")
    baseline_metrics = collect_metrics()

    print("\nColetando métricas MLOps DevSecOps...")
    mlops_metrics = collect_metrics()

    compare_metrics(baseline_metrics, mlops_metrics)
