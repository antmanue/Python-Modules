from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    healing_factory = HealingCreatureFactory()
    base_heal_creature = healing_factory.create_base()
    print(base_heal_creature.describe())
    print(base_heal_creature.attack())
    print(base_heal_creature.heal())  # type: ignore[attr-defined]
    print(" evolved:")
    evolved_heal_creature = healing_factory.create_evolved()
    print(evolved_heal_creature.describe())
    print(evolved_heal_creature.attack())
    print(evolved_heal_creature.heal())  # type: ignore[attr-defined]
    print()
    print("Testing Creature with transform capability")
    print(" base:")
    transform_factory = TransformCreatureFactory()
    base_transform_creature = transform_factory.create_base()
    print(base_transform_creature.describe())
    print(base_transform_creature.attack())
    print(base_transform_creature.transform())  # type: ignore[attr-defined]
    print(base_transform_creature.attack())
    print(base_transform_creature.revert())  # type: ignore[attr-defined]
    print(" evolved:")
    evolved_transform_creature = transform_factory.create_evolved()
    print(evolved_transform_creature.describe())
    print(evolved_transform_creature.attack())
    print(evolved_transform_creature.transform())  # type: ignore[attr-defined]
    print(evolved_transform_creature.attack())
    print(evolved_transform_creature.revert())  # type: ignore[attr-defined]


if __name__ == "__main__":
    test_healing_factory()
