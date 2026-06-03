 from ex0 import FlameFactory, AquaFactory

 def test_factory(factory) -> None:
    print("Testing factory")
    firebase = factory.create_base()
    print(f"{firebase.describe()}")
    print(f"{firebase.attack()}")

    fireevo = factory.create_evolved()
    print(f"{fireevo.describe()}")
    print(f"{fireevo.attack()}")

if __name__ == "__main__":
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()

    test_factory(flame_fac)
    test_factory(aqua_fac)