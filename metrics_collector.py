import json
import glob
import os

def read_json_file(path):
    if not os.path.exists(path):
        print(f"Aviso: arquivo não encontrado {path}")
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except UnicodeDecodeError:
        try:
            with open(path, "r", encoding="utf-16") as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao ler JSON: {path} -> {e}")
            return None
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

def count_bandit_issues(data):
    if not data or "metrics" not in data:
        return 0
    totals = data["metrics"].get("_totals", {})
    return sum([
        totals.get("SEVERITY.HIGH", 0),
        totals.get("SEVERITY.MEDIUM", 0),
        totals.get("SEVERITY.LOW", 0)
    ])

def count_safety_issues(data):
    if not data:
        return 0
    if "vulnerabilities" in data:
        return len(data["vulnerabilities"])
    return 0

def count_trivy_issues(data):
    if not data:
        return 0
    if isinstance(data, list):
        return len(data)
    elif isinstance(data, dict):
        return len(data.get("Results", []))
    return 0

baseline_path = "reports"
mlops_path = "reports"

bandit_baseline = count_bandit_issues(read_json_file(os.path.join(baseline_path, "bandit_report.json")))
bandit_mlops = count_bandit_issues(read_json_file(os.path.join(mlops_path, "bandit_report.json")))

safety_baseline = count_safety_issues(read_json_file(os.path.join(baseline_path, "safety_report.json")))
safety_mlops = count_safety_issues(read_json_file(os.path.join(mlops_path, "safety_report.json")))

trivy_baseline = count_trivy_issues(read_json_file(os.path.join(baseline_path, "trivy_report.json")))
trivy_mlops = count_trivy_issues(read_json_file(os.path.join(mlops_path, "trivy_report.json")))

train_baseline = read_train_time(os.path.join(baseline_path, "train_time_baseline.txt"))
train_mlops = read_train_time(os.path.join(mlops_path, "train_time_mlops.txt"))

print("\n--- Comparação de Métricas ---")
print(f"Bandit: Baseline = {bandit_baseline}, MLOps = {bandit_mlops}")
print(f"Safety: Baseline = {safety_baseline}, MLOps = {safety_mlops}")
print(f"Trivy: Baseline = {trivy_baseline}, MLOps = {trivy_mlops}")
print(f"TrainTime(s): Baseline = {train_baseline}, MLOps = {train_mlops}")
