from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        TransformCapability.__init__(self)
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if self.is_transformed is True:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        if self.is_transformed is False:
            self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        if self.is_transformed is True:
            self.is_transformed = False
        return "Shiftling returns to normal."


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        TransformCapability.__init__(self)
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self.is_transformed is True:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        if self.is_transformed is False:
            self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        if self.is_transformed is True:
            self.is_transformed = False
        return "Morphagon stabilizes its form."
