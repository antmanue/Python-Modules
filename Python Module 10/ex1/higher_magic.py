from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def amplified_power(target: str, power: int) -> str:
        new_power = power * multiplier

        return base_spell(target, new_power)
    return amplified_power


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def sequence_caster(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence_caster


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Restores{target} for {power} HP"

    print("--- Testing Spell Combiner ---")
    combo = spell_combiner(fireball, heal)
    print(combo("Dragon", 25))

    print("\n--- Testing Conditional Caster ---")

    def high_power_only(tgt: str, pwr: int) -> bool:
        return pwr > 50

    secure_cast = conditional_caster(high_power_only, fireball)
    print(f"Power 30: {secure_cast('Wizard', 30)}")
    print(f"Power 80: {secure_cast('Wizard', 80)}")

    print("\n--- Testing Spell Sequence ---")
    sequence = spell_sequence([fireball, heal, fireball])
    print(sequence("Knight", 15))
