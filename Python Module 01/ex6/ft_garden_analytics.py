class Plant:
     def __init__ (self, name: str, height: float, current_age: int, grow_rate: float) -> None:
        self._name = name
        self._grow_rate = grow_rate
        self._stats = Plant._Stats()
    

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
        
    class _Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def display(self) -> str:
            return f"Stats: {self._grow_count} grow, {self._age_count} age, {self._show_count} show"

    def get_stats(self) -> str:
        return self._stats.display()

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0, 0.0)

    @staticmethod
    def check_year(current_age: int) -> bool:
        if current_age > 365:
            return True
        else:
            return False

    def show(self) -> None:
        print(f"{self._name.capitalize()}: {self._height:.1f}cm, {self._current_age} days old")
        self._stats.increment_show()

    def grow(self) -> None:
        self._height += self._grow_rate
        self._stats.increment_grow()

    def age(self) -> None:
        self._current_age += 1
        self._stats.increment_age()

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

class Seed(Flower._Stats):
    def super().__init__(self) -> None:

    def get_name(self) -> str:

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


class Seed(Flower):
    def super().__init__(self) -> None:

    def get_name(self) -> str:


class Tree(Plant):

    def __init__(self, name: str, height: float, current_age: int, grow_rate: float, trunk_diameter: float):
        super().__init__(name, height, current_age, grow_rate)
        self._trunk_diameter = trunk_diameter
    
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0 
    
        def increment_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> str:
            return super().display() + f"self.{_shade_count} shade"


    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.increment_shade()
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
        self._nutritional_value = self._nutritional_value + 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")
