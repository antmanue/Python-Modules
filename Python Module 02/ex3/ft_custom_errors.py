class GardenError (Exception):
    def __init__ (self, message="Unknown garden error"):
        super().__init__(message)

class PlantError (GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)

def check_plant_health(is_wilting: bool) -> None:
    if is_wilting == True:
        raise PlantError("The tomato plant is wilting!")

def check_water_level(w_level: int) -> None:
    if w_level < 10:
        raise WaterError("Not enough water in the tank!")

def test_custom_errors() -> None:
        print(f"Testing PlantError...")
    try:
        check_plant_health(True)

    except PlantError as p_err:
        print(f"Caught PlantError: {p_err}")

    print(f"Testing WaterError...")     
     try:
        check_water_level(True)
    except WaterError as w_err:
        print(f"Caught WaterError: {w_err}")

def main() -> None:
    test_custom_errors()

if __name__ == "__main__":
    main()

