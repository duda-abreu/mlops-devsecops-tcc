import json
import os
import sys

def read_time(file):
    try:
        with open(file) as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0
    except Exception as e:
        sys.stderr.write(f"[WARN] Erro ao ler {file}: {e}\n")
        return 0

def main(reports_dir):
    metrics = {}
    steps = ["lint", "test", "bandit", "safety", "trivy", "train"]

    total_time = 0
    for step in steps:
        t = read_time(os.path.join(reports_dir, f"{step}_time.txt"))
        metrics[step] = f"{t}s"
        total_time += t

    metrics["total_pipeline_time"] = f"{total_time}s"

    baseline_file = os.path.join(reports_dir, "..", "baseline", "reports", "train_time_baseline.txt")
    if os.path.exists(baseline_file):
        baseline_time = read_time(baseline_file)
        if baseline_time > 0:
            diff = ((total_time - baseline_time) / baseline_time) * 100
            metrics["diff_vs_baseline"] = f"{diff:.2f}%"
        else:
            metrics["diff_vs_baseline"] = "N/A"

    bandit_file = os.path.join(reports_dir, "bandit_report.json")
    if os.path.exists(bandit_file):
        try:
            with open(bandit_file) as f:
                bandit_data = json.load(f)
                if "_totals" in bandit_data.get("metrics", {}):
                    metrics["bandit_totals"] = bandit_data["metrics"]["_totals"]
                for file_path, file_metrics in bandit_data.get("metrics", {}).items():
                    if file_path != "_totals":
                        metrics.setdefault("bandit_files", {})[file_path] = file_metrics
        except Exception as e:
            sys.stderr.write(f"[WARN] Erro ao ler Bandit JSON: {e}\n")

    output_file = os.path.join(reports_dir, "metrics_summary.json")
    with open(output_file, "w") as f:
        json.dump(metrics, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python metrics.py <reports_dir>")
        sys.exit(1)
    main(sys.argv[1])
