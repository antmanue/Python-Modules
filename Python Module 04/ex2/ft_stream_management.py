import sys

def process_archive() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_stream_management.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    
    try:
        current_file = sys.argv[1]
        file = open(sys.argv[1])
        original_txt = file.read()
        file.close()

        print("---")
        print()
        print(f"{original_txt}", end="")
        print()
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
        print()

        print("Transform data:")
        print("---")
        print()

        list_lines = original_txt.splitlines()
        transformed_lines = []
        for line in list_lines:
            line_with_hash = f"{line}#"
            print(line_with_hash)
            transformed_lines.append(line_with_hash)
        
        print()
        print("---")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_file = sys.stdin.readline().rstrip("\n")
        current_file = new_file

        if not new_file:
            print("Not saving data.")
            return
        
        print(f"Saving data to '{new_file}'")

        content_to_save = "\n".join(transformed_lines) + "\n"
        out_file = open(new_file, "w")
        out_file.write(content_to_save)
        out_file.close()

        print(f"Data saved in file '{new_file}'.")

    except Exception as err:
        sys.stderr.write(f"[STDERR] Error opening file '{current_file}': {err}\n")
        if current_file != sys.argv[1]:
            print("Data not saved.")


def main() -> None:
    process_archive()


if __name__ == "__main__":
    main()