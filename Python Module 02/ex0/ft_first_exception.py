def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except ValueError as err:
        print(f"Caught input_temprature error: {err}")
        return 0

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")
    print(f"Input data is '25'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}°C")
    print("")
    print(f"Input data is 'abc'")
    input_temperature("abc")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()