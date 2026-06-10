import importlib
import sys

def check_dependencies() -> bool:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    modules_to_check: list[str] = ["pandas", "numpy", "requests", "matplotlib"]
    readiness_messages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }

    all_good = True

    for i in modules_to_check:
        try:
            module = importlib.import_module(i)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {i} ({version} readiness_messages[i]")
        except ModuleNotFoundError as err:
            print(f"[ERROR] Dependency missing: {err}")
            print("Use pip install -r requirements.txt ou poetry install")
            all_good = False

    if not all_good:
        print("Analyzing Matrix data...")
        print("Processing 1000 data points")
        return False
    
    return True

def run_analysis() -> None:

    import matplotlib.pyplot as plt
    import numpy as np

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    matrix_data = np.random.rand(1000)

    print("Generating visualization...")

    plt.figure(figsize=(10, 6))
    plt.hist(matrix_data, bins=50, color='green', alpha=0.7)
    plt.title("Matrix Data Stream Analysis")
    plt.xlabel("Data Points Value")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle='--', alpha=0.5)

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")

def main() -> None:
    if check_dependencies():
        run_analysis()
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()