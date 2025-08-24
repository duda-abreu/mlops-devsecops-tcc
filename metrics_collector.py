import json
import os

BANDIT_PATH = "reports/bandit_report.json"
SAFETY_PATH = "reports/safety_report.json"
TRIVY_PATH = "reports/trivy_report.json"
TRAIN_TIME_PATH_BASELINE = "reports/train_time_baseline.txt"
TRAIN_TIME_PATH_MLOPS = "reports/train_time_mlops.txt"

def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"Erro ao ler JSON: {file_path}")
                return {}
    return {}

def read_train_time(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return None
    return None

def count_vulnerabilities(report, key=None):
    if not report:
        return 0
    if key:  
        return len(report.get(key, []))
    return len(report.get("results", [])) if "results" in report else len(report)

def collect_metrics():
    metrics = {}

    metrics["baseline"] = {
        "Bandit": count_vulnerabilities(read_json(BANDIT_PATH)),
        "Safety": count_vulnerabilities(read_json(SAFETY_PATH)),
        "Trivy": count_vulnerabilities(read_json(TRIVY_PATH), key="Results"),
        "TrainTime(s)": read_train_time(TRAIN_TIME_PATH_BASELINE)
    }

    metrics["mlops"] = {
        "Bandit": count_vulnerabilities(read_json(BANDIT_PATH)),
        "Safety": count_vulnerabilities(read_json(SAFETY_PATH)),
        "Trivy": count_vulnerabilities(read_json(TRIVY_PATH), key="Results"),
        "TrainTime(s)": read_train_time(TRAIN_TIME_PATH_MLOPS)
    }

    return metrics

def print_comparison(metrics):
    print("\n--- Comparação de Métricas ---")
    for key in ["Bandit", "Safety", "Trivy", "TrainTime(s)"]:
        baseline_val = metrics["baseline"].get(key)
        mlops_val = metrics["mlops"].get(key)
        print(f"{key}: Baseline = {baseline_val}, MLOps = {mlops_val}")

if __name__ == "__main__":
    metrics = collect_metrics()
    print_comparison(metrics)
