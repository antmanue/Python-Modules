import functools
import operator
from typing import Callable, Any

OPERATIONS: dict[str, Callable[[int, int], int]] = {
    "add": operator.add,
    "multiply": operator.mul
}


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "max":
        return functools.reduce(max, spells)  # type: ignore[call-overload]
    if operation == "min":
        return functools.reduce(min, spells)  # type: ignore[call-overload]

    if operation not in OPERATIONS:
        raise ValueError("Unknown Operation")
    return functools.reduce(OPERATIONS[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchant = functools.partial(base_enchantment, 50, "Fire")
    ice_enchant = functools.partial(base_enchantment, 50, "Ice")
    lightning_enchant = functools.partial(base_enchantment, 50, "Lightning")

    return {
        "fire": fire_enchant,
        "ice": ice_enchant,
        "lightning": lightning_enchant
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def _dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @_dispatcher.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @_dispatcher.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @_dispatcher.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return _dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTeste fibonacci")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")

    print("\nTesting spell dispatcher")
    dispatcher = spell_dispatcher()
    print(dispatcher(100))
    print(dispatcher("Fireball"))
    print(dispatcher([1, 2, 3]))

    print("\nTesting partial enchanter...")

    def demo_enchant(power: int, element: str, target: str) -> str:
        return f"Casting {element} spell wit {power} power on {target}"

    enchanters = partial_enchanter(demo_enchant)
    print(enchanters["fire"]("Goblin"))
    print(enchanters["ice"]("Dragoon"))
