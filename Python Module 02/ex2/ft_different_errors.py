def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1/0
    elif operation_number == 2:
        open("notafile.txt")
    elif operation_number == 3:
        "abc" + 4

def test_error_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")

        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
       
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        
        else:
            print(f"Operation completed successfully")
    print()
    print(f"All error types tested successfully!")


def main() -> None:
    print("=== Garden Types Demo ===")
    test_error_types()

if __name__ == "__main__":
    main()