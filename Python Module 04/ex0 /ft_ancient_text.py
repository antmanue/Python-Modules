import sys

def input_check() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    
    try:
        file = open(sys.argv[1])
        print(f"{file.read()}")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except Exception as err:
        print(f"Error opening file '{sys.argv[1]}': {err}")


def main() -> None:
    input_check()

if __name__ == "__main__":
    main()