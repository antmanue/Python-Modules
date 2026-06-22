from collections.abc import Callable

def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
    ) -> Callable[[str, int], tuple[str, str]]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell

def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int) -> Callable[[str, int], str]:
    def amplified_power(target: str, power: int) -> str:
        new_power = power * multiplier

        return base_spell(target, new_power)
    return amplified_power