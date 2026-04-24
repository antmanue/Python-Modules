# #!/usr/bin/env python3
# --Criacao de class Plant-- #
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, {self.age} days old")


rose_plant = Plant("Rose", 25, 30)
sunflower_plant = Plant("Sunflower", 80, 45)
cactus_plant = Plant("Cactus", 15, 120)
garden = [rose_plant, sunflower_plant, cactus_plant]


def main() -> None:
    print("=== Garden Plant Registry ===")
    for plant in garden:
        plant.show()


if __name__ == "__main__":
    main()
