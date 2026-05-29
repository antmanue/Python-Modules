def secure_archive(file_name: str,
                   action: str = "",
                   text_to_save: str = ""
                   ) -> tuple[bool, str]:
    try:
        if action in ("r", "read", "R", "READ", 1):
            with open(file_name, "r") as file:
                content = file.read()
            return (True, content)

        elif action in ("w", "write", "W", "WRITE", 2):
            with open(file_name, "w") as file:
                file.write(text_to_save)
            return (True, "Content successfully written to file")

        else:
            return (False, "Invalid action. Use 'r' "
                           "for read or 'w' for write.")

    except Exception as err:
        return (False, f"{err}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from an nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/home/antarva/Documents/42_Porto"
                         "/Common_Core/Milestone_02/"
                         "Python-Modules/Python Module"
                         "04/ex3/denied.txt", "r"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive(
        "/home/antarva/Documents/42_Porto/"
        "Common_Core/Milestone_02/Python-Modules/"
        "Python Module 04/ex3/ancient_fragment.txt", "r"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive(
        "/home/antarva/Documents/42_Porto/Common_Core/"
        "Milestone_02/Python-Modules/Python Module 04"
        "/ex3/new_vault_file.txt", "w",
        text_to_save="Novo teste!"
        ))


if __name__ == "__main__":
    main()
