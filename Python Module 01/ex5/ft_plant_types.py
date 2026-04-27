class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, grow_rate: float, color: str):
        super().__init__(name, height, age, grow_rate)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
    
    def bloom(self) -> None:
        print(f"{self._name.capitalize()} is blooming beautifully!")

class Tree(Plant):

    def __init__(self, name: str, height: float, age: int, grow_rate: float, trunk_diameter: float):
        super().__init__(name, height, age, grow_rate)
        self._trunk_diameter = trunk_diameter
    
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")
    
    def produce_shade(self) -> 


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int, grow_rate: float, harvest_season: str):
        super super(),__init__(name, height, age, grow_rate)
        self._nutritional_value = 0
        self._harvest_season = harvest_season
    
    def show(self) -> None:
        super().show()
        print(f"Nutritional Value: {self._nutritional_value}")