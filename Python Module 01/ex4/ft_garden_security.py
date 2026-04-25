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

def main() -> None:
    print("=== Garden Security System ===")
    rose_plant = Plant("Rose", 15.0, 10, 0.8)
    print("Plant Created: ", end="")
    rose_plant.show()
    print("")
    rose_plant.set_height(25)
    rose_plant.set_age(30)
    print("")
    rose_plant.set_height(-5)
    rose_plant.set_age(-10)
    print("")
    print("")
    print("Current state: ", end="")
    rose_plant.show()

if __name__ == "__main__":
    main()
