from ex0 import FlameFactory, AquaFactory

def test_factory(factory) -> None:
    print("Testing factory")
    firebase = factory.create_base()
    print(f"{firebase.describe()}")
    print(f"{firebase.attack()}")

    fireevo = factory.create_evolved()
    print(f"{fireevo.describe()}")
    print(f"{fireevo.attack()}")

def test_battle(factory1, factory2) -> None:
    print("Testing battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(f"{creature1.describe()}")
    print(" vs.")
    print(f"{creature2.describe()}")
    print(" fight!")
    print(f"{creature1.attack()}")
    print(f"{creature2.attack()}")

if __name__ == "__main__":
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    test_factory(flame_fac)
    print()
    test_factory(aqua_fac)
    print()
    test_battle(flame_fac, aqua_fac)
