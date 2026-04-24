class Plant:
    def __init__(self, name: str, height: float, current_age: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.current_age = current_age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"Created: {self.name.capitalize()}: "
              f"{self.height:.1f}cm, {self.current_age} days old")

    def age(self) -> None:
        self.current_age += 1

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

def main() -> None:
    rose_plant = Plant("Rose", 25, 30, 0.8)
    oak_plant = Plant("Oak", 200, 365, 0.5)
    cactus_plant = Plant("Cactus", 5, 90, 0.2)
    sunflower_plant = Plant("Sunflower", 80, 45, 1.5)
    fern_plant = Plant("Fern", 15, 120, 0.3)

    garden = [rose_plant, oak_plant, cactus_plant, sunflower_plant, fern_plant]
    
    for plant in garden:
        plant.show()

if __name__ == "__main__":
    main()