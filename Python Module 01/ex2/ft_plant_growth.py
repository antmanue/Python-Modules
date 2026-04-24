# #!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, current_age: int) -> None:
        self.name = name
        self.height = height
        self.current_age = current_age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, {self.current_age} days old")

    def age(self, days: int) -> None:
        self.current_age += days

    def grow(self, extra_cm: float) -> None:
        self.height += extra_cm

rose_plant = Plant("Rose", 25, 30)
#sunflower_plant = Plant("Sunflower", 80, 45)
#cactus_plant = Plant("Cactus", 15, 120)
#garden = [rose_plant, sunflower_plant, cactus_plant]


def main() -> None:
    print("=== Garden Plant Registry ===")
    rose_plant.show()
    initial_height = rose_plant.height
    for day in range(1, 8):
        print(f"== Day {day} ==")
        rose_plant.age(1)
        rose_plant.grow(0.8)
        rose_plant.show()
    total_growth = round(rose_plant.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")

if __name__ == "__main__":
    main()
