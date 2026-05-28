import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if sys.argv[1:]:
        print(f"Arguments received: {len(sys.argv) - 1}")
        count: int = 1
        for arg in sys.argv[1:]:
            print(f"Argument {count}: {arg}")
            count += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
