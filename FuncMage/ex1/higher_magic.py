from typing import Callable

def spell(target: str, power: int) -> str:
    return f"{target} is hit with a spell of power {power}!"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def fireball(target: str, power: int) -> str:
    return f"{target} is engulfed in a fireball of power {power}!"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def Integration(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return Integration

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)
    return amplify

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def throw(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return throw

def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        lis: list[str] = []
        for spell in spells:
            lis.append(spell(target, power))
        return lis
    return sequence

def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal) 
    output = combined("Dragon", 20)
    print(f"Combined spell result: {output[0]}, {output[1]}")

    print("\n")

    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {amplified('Dragon', 10)}")

if __name__ == "__main__":
    main()