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
    def __init__(self, name: str, height: float, current_age: int, grow_rate: float, color: str) -> None:
        super().__init__(name, height, current_age, grow_rate, color)
        self._seed_count = 0
    
    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")
    
    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

class Tree(Plant):

    def __init__(self, name: str, height: float, current_age: int, grow_rate: float, trunk_diameter: float):
        super().__init__(name, height, current_age, grow_rate)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree._TreeStats()
    
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0 
    
        def increment_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> str:
            return super().display() + f"\n {self._shade_count} shade."


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

def display_any(plant: Plant) -> None:
    print(f"{plant.get_stats()}")

def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print (f"Is 30 days more than a year? -> {Plant.check_year(30)}")
    print (f"Is 400 days more than a year? -> {Plant.check_year(400)}")
    print("")
    print("=== Flower")
    rose_plant = Flower("rose", 15.0, 10, 8.0, "red")
    rose_plant.show()
    print(f"[statistics for {rose_plant._name.capitalize()}]")
    display_any(rose_plant)
    print(f"[asking the {rose_plant._name} to grow and bloom]")
    rose_plant.grow()
    rose_plant.bloom()
    rose_plant.show()
    print(f"[statistics for {rose_plant._name.capitalize()}]")
    display_any(rose_plant)
    print("")
    print("=== Tree")
    oak_tree = Tree("oak", 200.0, 365, 0.0, 5.0)
    oak_tree.show()
    print(f"[statistics for {oak_tree._name.capitalize()}]")
    display_any(oak_tree)
    print(f"[asking the {oak_tree._name} to produce shade]")
    oak_tree.produce_shade()
    display_any(oak_tree)
    print("")
    print("=== Seed")
    sun_seed = Seed("sunflower", 80.0, 45, 30.0, "yellow")
    sun_seed.show()
    print(f"[make {sun_seed._name} grow, age, and bloom]")
    sun_seed.grow()
    sun_seed.age()
    sun_seed._current_age += 19 
    sun_seed.bloom()
    sun_seed.show()
    print(f"[statistics for {sun_seed._name.capitalize()}]")
    display_any(sun_seed)
    print("")
    print("=== Anonymous")
    unknown_plant = Plant.create_anonymous()
    unknown_plant.show()
    print(f"[statistics for Unknown plant]")
    display_any(unknown_plant)

if __name__ == "__main__":
    main()
