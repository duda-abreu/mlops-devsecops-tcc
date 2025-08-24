import json
import os

def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                print(f"Erro ao ler JSON: {file_path}")
                return {}
    return {}

def read_train_time(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return float(f.read().strip())
            except ValueError:
                return None
    return None

def count_bandit_issues(data):
    if not data:
        return 0
    return len(data.get("results", []))

def count_safety_issues(data):
    if not data:
        return 0
    return len(data.get("vulnerabilities", []))

def count_trivy_issues(data):
    if not data:
        return 0
    return len(data.get("Results", []))

paths = {
    "baseline": {
        "bandit": "reports/baseline_bandit_report.json",
        "safety": "reports/baseline_safety_report.json",
        "trivy": "reports/baseline_trivy_report.json",
        "train": "reports/train_time_baseline.txt"
    },
    "mlops": {
        "bandit": "reports/bandit_report.json",
        "safety": "reports/safety_report.json",
        "trivy": "reports/trivy_report.json",
        "train": "reports/train_time_mlops.txt"
    }
}

metrics = {}
for key, files in paths.items():
    bandit_data = read_json(files["bandit"])
    safety_data = read_json(files["safety"])
    trivy_data = read_json(files["trivy"])
    train_time = read_train_time(files["train"])

    metrics[key] = {
        "Bandit": count_bandit_issues(bandit_data),
        "Safety": count_safety_issues(safety_data),
        "Trivy": count_trivy_issues(trivy_data),
        "TrainTime(s)": train_time
    }

print("\n--- Comparação de Métricas ---")
for metric in ["Bandit", "Safety", "Trivy", "TrainTime(s)"]:
    baseline_val = metrics["baseline"].get(metric)
    mlops_val = metrics["mlops"].get(metric)
    print(f"{metric}: Baseline = {baseline_val}, MLOps = {mlops_val}")
