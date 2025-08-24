import json
import os

baseline_dir = "baseline-reports"
mlops_dir = "mlops-reports"

def count_bandit_vulns(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path) as f:
        data = json.load(f)
    return len(data.get("results", []))

def count_safety_vulns(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path) as f:
        data = json.load(f)
    return len(data.get("vulnerabilities", []))

def count_trivy_vulns(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path) as f:
        data = json.load(f)
    return sum(len(r.get("Vulnerabilities", [])) if r.get("Vulnerabilities") else 0 for r in data)

def read_train_time(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path) as f:
        line = f.readline().strip()
    parts = line.split()
    return int(parts[-2]) if len(parts) >= 3 else None

baseline_metrics = {
    "Bandit": count_bandit_vulns(os.path.join(baseline_dir, "bandit_report.json")),
    "Safety": count_safety_vulns(os.path.join(baseline_dir, "safety_report.json")),
    "Trivy": count_trivy_vulns(os.path.join(baseline_dir, "trivy_report.json")),
    "TrainTime(s)": read_train_time(os.path.join(baseline_dir, "train_time_baseline.txt"))
}

mlops_metrics = {
    "Bandit": count_bandit_vulns(os.path.join(mlops_dir, "bandit_report.json")),
    "Safety": count_safety_vulns(os.path.join(mlops_dir, "safety_report.json")),
    "Trivy": count_trivy_vulns(os.path.join(mlops_dir, "trivy_report.json")),
    "TrainTime(s)": read_train_time(os.path.join(mlops_dir, "train_time_mlops.txt"))
}

print("\n--- Comparação de Métricas ---")
for key in baseline_metrics.keys():
    print(f"{key}: Baseline = {baseline_metrics[key]}, MLOps = {mlops_metrics[key]}")
