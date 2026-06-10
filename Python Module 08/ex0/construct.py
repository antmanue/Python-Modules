import sys
import site
import os


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_virtual_env():

        venv_name: str = os.path.basename(sys.prefix)

        pkg_path: str = site.getsitepackages()[0]

        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print(f"Package installation path:\n {pkg_path}")
    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machine can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix-env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
