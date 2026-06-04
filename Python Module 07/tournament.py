import ex0
import ex2
from ex2.strategies import BattleStrategy


class Opponent:
    def __init__(self, creature: ex0.Creature,
                 strategy: BattleStrategy) -> None:
        self.creature = creature
        self.strategy = strategy

    def __repr__(self) -> str:
        creature_class = type(self.creature).__name__
        strat_class = type(self.strategy).__name__.replace("Strategy", "")
        return f"({creature_class}+{strat_class})"


class Flameling(ex0.Creature):
    def __init__(self) -> None:
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        return "Flameling uses Ember!"

    def __str__(self) -> str:
        return "Flameling is a Fire type Creature"


class Aquabub(ex0.Creature):
    def __init__(self) -> None:
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"

    def __str__(self) -> str:
        return "Aquabub is a Water type Creature"


class Healing(ex0.Creature):
    def __init__(self) -> None:
        self.name = "Sproutling"
        self.type = "Grass"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"

    def __str__(self) -> str:
        return "Sproutling is a Grass type Creature"


class Transform(ex0.Creature):

    def __init__(self) -> None:
        self.name = "Shiftling"
        self.type = "Normal"

    def attack(self) -> str:
        return ("Shiftling performs a boosted strike"
                "!\nShiftling returns to normal.")

    def transform(self) -> str:
        return "Shiftling shifts into a sharper form!"

    def __str__(self) -> str:
        return "Shiftling is a Normal type Creature"


def run_tournament(title: str, opponents: list) -> None:
    print(title)
    print("[ " + ", ".join(repr(opp) for opp in opponents) + " ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:

        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                opp1 = opponents[i]
                opp2 = opponents[j]
                print()
                print("* Battle *")
                print(opp1.creature)
                print("vs.")
                print(opp2.creature)
                print("now fight!")
                print(opp1.strategy.act(opp1.creature))
                print(opp2.strategy.act(opp2.creature))
    except ex2.InvalidStrategy as err:
        print(f"Battle error, aborting tournament: {err}")
    print()


def main() -> None:
    normal = ex2.NormalStrategy()
    aggressive = ex2.AggressiveStrategy()
    defensive = ex2.DefensiveStrategy()

    flameling = Flameling()
    sproutling = Healing()
    aquabub = Aquabub()
    shiftling = Transform()

    opponents_0 = [
        Opponent(flameling, normal),
        Opponent(sproutling, defensive),
        ]
    run_tournament("Tournament 0 (basic)", opponents_0)

    opponents_1 = [
        Opponent(flameling, aggressive),
        Opponent(sproutling, defensive),
        ]
    run_tournament("Tournament 1 (error)", opponents_1)

    opponents_2 = [
        Opponent(aquabub, normal),
        Opponent(sproutling, defensive),
        Opponent(shiftling, aggressive)
        ]
    run_tournament("Tournament 2 (multiple)", opponents_2)


if __name__ == "__main__":
    main()
