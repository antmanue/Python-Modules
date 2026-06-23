from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:

        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    current_total = initial_power

    def accumulator(amount: int) -> int:
        nonlocal current_total
        current_total += amount
        return current_total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanter(item_name: str) -> str:

        return f"{enchantment_type} {item_name}"
    return enchanter


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key in vault:
            return vault[key]
        else:
            return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Teste mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flaming_enchanter = enchantment_factory("Flaming")
    frozen_enchanter = enchantment_factory("Frozen")

    print(flaming_enchanter("Sword"))
    print(frozen_enchanter("Shield"))

    print("\nTesting memory vault...")
    vault_funcs = memory_vault()

    print("Store 'secret' = 42")
    vault_funcs["store"]("secret", 42)
    print(f"Recall 'secret': {vault_funcs['recall']('secret')}")
    print(f"Recall 'unknown': {vault_funcs['recall']('unknown')}")
