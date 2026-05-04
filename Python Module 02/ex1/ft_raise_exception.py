def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        return temp
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
        return 0

def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    
    print()
    print(f"Input data is '25'")
    temp = input_temperature("25")
    
    print()
    print(f"Input data is 'abc'")
    input_temperature("abc")
    
    print()
    print(f"Input data is '100'")
    temp = input_temperature("100")
    
    print()
    print(f"Input data is '-50'")
    input_temperature("-50")
    
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()