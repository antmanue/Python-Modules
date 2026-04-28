class Plant:
    def __init__ (self, name: str, height: float, current_age: int, grow_rate: float) -> None:
        self._name = name
        self._grow_rate = grow_rate
        
        if height < 0:
            self._height = 0.0
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

        if current_age < 0:
            self._current_age = 0
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._current_age = current_age

    def show(self) -> None:
        print(f"{self._name.capitalize()}: {self._height:.1f}cm, {self._current_age} days old")

    def grow(self) -> None:
        self._height += self._grow_rate

    def age(self) -> None:
        self._current_age += 1
    
    def get_height(self) -> float:
        return(self._height)

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

        else:
            self._height = new_height
            print(f"Height updated: {int(new_height)}cm")

    def get_age(self) -> int:
        return(self._current_age)

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

        else:
            self._current_age = new_age
            print(f"Age updated: {new_age} days")

class Flower(Plant):

    def __init__(self, name: str, height: float, current_age: int, grow_rate: float, color: str):
        super().__init__(name, height, current_age, grow_rate)
        self._color = color
        self._has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed == False:
            print(f"{self._name.capitalize()} has not bloomed yet")
        if self._has_bloomed == True:
            print(f"{self._name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        if self._has_bloomed == False:
            self._has_bloomed = True

class Tree(Plant):

    def __init__(self, name: str, height: float, current_age: int, grow_rate: float, trunk_diameter: float):
        super().__init__(name, height, current_age, grow_rate)
        self._trunk_diameter = trunk_diameter
    
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")
    
    def produce_shade(self) -> None:
        print(f"Tree {self._name.capitalize()} now produces a shade of {self._height:.1f}cm "
              f"long and {self._trunk_diameter:.1f}cm wide")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, current_age: int, grow_rate: float, harvest_season: str):
        super().__init__(name, height, current_age, grow_rate)
        self._nutritional_value = 0
        self._harvest_season = harvest_season

    def grow(self) -> None:
        super().grow()
        self._nutritional_value = self._nutritional_value + 1

    
    def age(self) -> None:
        super().age()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional Value: {self._nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose_plant = Flower("Rose", 15.0, 10, 0.8, "red")
    rose_plant.show()
    print(f"[asking the {rose_plant._name} to bloom]")
    rose_plant.bloom()
    rose_plant.show()
    print("")
    print("=== Tree")
    oak_tree = Tree("oak", 200.0, 365, 0.5, 5.0)
    oak_tree.show()
    print(f"[asking the {oak_tree._name} to produce shade]")
    oak_tree.produce_shade()
    print("")
    print("=== Vegetable")
    tomato_veg = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    tomato_veg.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato_veg.grow()
        tomato_veg.age()
    tomato_veg.show()

if __name__ == "__main__":
    main()
