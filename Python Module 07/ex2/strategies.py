from abc import ABC, abstractmethod
from ex0 import Creature


class InvalidStrategy(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if hasattr(creature, "transform"):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature) is True:
            msg_transform = creature.transform()  # type: ignore[attr-defined]
            msg_attack = creature.attack()
            return f"{msg_transform}\n{msg_attack}"
        name = getattr(creature, "name", "Unknown")
        raise InvalidStrategy(f"Invalid Creature '{name}' for this "
                              f"aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if hasattr(creature, "heal"):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature) is True:
            msg_attack = creature.attack()
            msg_heal = creature.heal()  # type: ignore[attr-defined]
            return f"{msg_attack}\n{msg_heal}"

        name = getattr(creature, "name", "Unknown")
        raise InvalidStrategy(f"Invalid Creature '{name}' "
                              f"for this defensive strategy")
