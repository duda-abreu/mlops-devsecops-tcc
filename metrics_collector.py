import json
import glob
import os
import time

BANDIT_REPORT = "bandit_report.json"
TRIVY_REPORT = "trivy_report.json"
TRAIN_BASELINE_FILE = "train_time_baseline.txt"
TRAIN_MLOPS_FILE = "train_time_mlops.txt"

def read_json_file(path):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except UnicodeDecodeError:
        with open(path, "r", encoding="utf-16") as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao ler JSON: {path} -> {e}")
        return None

def read_train_time(file_pattern):
    files = glob.glob(file_pattern)
    if not files:
        return None
    try:
        with open(files[0], "r", encoding="utf-8") as f:
            content = f.read().strip()
            return int(content) if content else None
    except Exception as e:
        print(f"Erro ao ler tempo de treino: {files[0]} -> {e}")
        return None

def bandit_severity(data):
    if not data or "metrics" not in data:
        return {"high": 0, "medium": 0, "low": 0}
    totals = data["metrics"].get("_totals", {})
    return {
        "high": totals.get("SEVERITY.HIGH", 0),
        "medium": totals.get("SEVERITY.MEDIUM", 0),
        "low": totals.get("SEVERITY.LOW", 0),
    }

def count_safety_issues(data):
    if not data or "scan_results" not in data:
        return 0
    count = 0
    for project in data["scan_results"].get("projects", []):
        for file in project.get("files", []):
            for dep in file.get("results", {}).get("dependencies", []):
                count += len(dep.get("vulnerabilities", {}).get("known_vulnerabilities", []))
    return count

def count_bandit_issues(data):
    if not data or "metrics" not in data:
        return 0
    totals = data["metrics"].get("_totals", {})
    return sum([
        totals.get("SEVERITY.HIGH", 0),
        totals.get("SEVERITY.MEDIUM", 0),
        totals.get("SEVERITY.LOW", 0)
    ])

def count_trivy_issues(data):
    if not data:
        return 0
    if isinstance(data, list):
        return len(data)
    elif isinstance(data, dict):
        return len(data.get("Results", []))
    return 0

def measure_execution_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, round(end - start, 2)

def diff(baseline, mlops):
    if baseline == 0:
        return "N/A" if mlops == 0 else "+∞%"
    return f"{((mlops - baseline)/baseline)*100:.1f}%"

baseline_path = "reports"
mlops_path = "reports"

bandit_baseline = count_bandit_issues(read_json_file(os.path.join(baseline_path, BANDIT_REPORT)))
bandit_mlops = count_bandit_issues(read_json_file(os.path.join(mlops_path, BANDIT_REPORT)))

safety_baseline = sum(
    count_safety_issues(read_json_file(f))
    for f in glob.glob(os.path.join(baseline_path, "*safety*.json"))
)
safety_mlops = sum(
    count_safety_issues(read_json_file(f))
    for f in glob.glob(os.path.join(mlops_path, "*safety*.json"))
)

bandit_result, bandit_time = measure_execution_time(
    count_bandit_issues,
    read_json_file(os.path.join(mlops_path, BANDIT_REPORT))
)

trivy_baseline = count_trivy_issues(read_json_file(os.path.join(baseline_path, TRIVY_REPORT)))
trivy_mlops = count_trivy_issues(read_json_file(os.path.join(mlops_path, TRIVY_REPORT)))

train_baseline = read_train_time(os.path.join(baseline_path, TRAIN_BASELINE_FILE))
train_mlops = read_train_time(os.path.join(mlops_path, TRAIN_MLOPS_FILE))

print("\n--- Comparação de Métricas ---")
print(f"Bandit: Baseline = {bandit_baseline}, MLOps = {bandit_mlops}")
print(f"Safety: Baseline = {safety_baseline}, MLOps = {safety_mlops}")
print(f"Trivy: Baseline = {trivy_baseline}, MLOps = {trivy_mlops}")
print(f"TrainTime(s): Baseline = {train_baseline}, MLOps = {train_mlops}")
print(f"Bandit issues: {bandit_result} (tempo: {bandit_time}s)")
