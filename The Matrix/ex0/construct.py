import sys
import site
import os

def main() -> None:
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You’re in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts/activate # On Windows")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You’re in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print(f"Package installation path: {site.getsitepackages()[0]}")

if __name__ == "__main__":
    main()