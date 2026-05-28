class GardenError (Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError (GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant_health(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_level(w_level: int) -> None:
    if w_level < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        check_plant_health(True)

    except PlantError as p_err:
        print(f"Caught PlantError: {p_err}")
    print()
    print("Testing WaterError...")
    try:
        check_water_level(5)
    except WaterError as w_err:
        print(f"Caught WaterError: {w_err}")
    print()
    print("Testing catching all garden errors...")
    try:
        check_plant_health(True)

    except GardenError as g_err:
        print(f"Caught GardenError: {g_err}")
    try:
        check_water_level(5)
    except GardenError as g_err:
        print(f"Caught GardenError: {g_err}")
    print()
    print("All error types tested successfully!")


def main() -> None:
    test_custom_errors()


if __name__ == "__main__":
    main()
