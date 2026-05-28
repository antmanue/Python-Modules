def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 4  # type: ignore[operator]


def test_error_types() -> None:
    i: int = 0
    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except (ValueError,
                ZeroDivisionError,
                FileNotFoundError,
                TypeError,
                ) as error:
            print(f"Caught {error.__class__.__name__}: {error}")
        else:
            print("Operation completed successfully")
        i = i + 1
    print()
    print("All error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    main()
