import sys
import importlib
import numpy
import pandas
import matplotlib.pyplot as plt
def check_dependencies() -> bool:
    val = True
    lis = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}
    print("Checking dependencies:")
    for i, j in lis.items():
        if importlib.util.find_spec(i):
            x = importlib.import_module(i)
            print(f"[OK] {i} ({x.__version__}) - {j}")

        else:
            print(f"[KO] {i} is missing! Install with pip or poetry.")
            val = False
    print("")
    return val


def create_visualization(df: pandas.DataFrame) -> None:
    print("Generating visualization...")
    plt.plot(df['Signal Value'], 'g', linewidth=0.5)
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Index")
    plt.ylabel("Signal Amplitude")
    
    plt.savefig("matrix_analysis.png")
    plt.close()
    
    
def main() -> None:
    print("LOADING STATUS: Initializing system check...\n")
    ready: bool = check_dependencies()
    if not ready:
        print("SYSTEM ERROR: Failed to load required programs.")
        sys.exit(1)
    print("SUCCESS: All programs loaded. Generating matrix data...")
    data = numpy.random.standard_normal(1000)
    df = pandas.DataFrame(data, columns=['Signal Value'])
    print(f"Processing {len(df)} data points...")
    create_visualization(df)
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")

if __name__ == "__main__":
    main()