from typing import Callable
def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter

def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power
    def total_energy(added: int) -> int:
        nonlocal total
        total += added
        return total
    return total_energy

def enchantment_factory(enchantment_type: str) -> Callable:
    
    def mascot(item_name: str) -> str:
        return f"{enchantment_type} {item_name}!"
    return mascot

def memory_vault() -> dict[str, Callable]:
    dicts = {}
    def store(key: str, value: Callable) -> None:
        dicts[key] = value
    def recall(key: str) -> Callable:
        return dicts.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    accumulator_a = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator_a(20)}")
    print(f"Base 100, add 30: {accumulator_a(30)}")
    print("\nTesting enchantment factory...")
    fire = enchantment_factory("Flaming")
    snow = enchantment_factory("Frozen")
    print(fire("Sword"))
    print(snow("Shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']("fire_spell", fire)
    vault['store']("snow_spell", snow)
    recall = vault['recall']
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")

if __name__ == "__main__":
    main()