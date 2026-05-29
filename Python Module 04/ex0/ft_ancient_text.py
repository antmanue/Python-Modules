import sys


def input_check() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        file = open(sys.argv[1], "r")
        print("---")
        print(file.read(), end="")
        file.close()
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as f_err:
        print(f"Error opening file '{sys.argv[1]}': {f_err}")
    except PermissionError as p_err:
        print(f"Error opening file '{sys.argv[1]}': {p_err}")
    except Exception as err:
        print(f"Error opening file '{sys.argv[1]}': {err}")


def main() -> None:
    input_check()


if __name__ == "__main__":
    main()
