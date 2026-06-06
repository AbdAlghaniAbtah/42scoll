import functools
from typing import Any, Callable, cast
import operator
def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }
    if not spells:
        return 0
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(operations[operation], spells)

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    dicts = {
        "flaming": functools.partial(base_enchantment, 50, "fire"),
        "freezing": functools.partial(base_enchantment, 50, "ice"),
        "shocking": functools.partial(base_enchantment, 50, "lightning")
    }
    return dicts

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(value: Any) -> str:
        return "Unknown spell type"
    @cast.register(str)
    def _(value: str) -> str:
        return value
    @cast.register(int)
    def _(value: int) -> str:
        if type(value) == int:
            return f"{value} damage"
        return "Unknown spell type"

    @cast.register(list)
    def _(value: list) -> str:
        return f"{len(value)} spells"

    return cast


def enchantment(power: int, element: str, target: str) -> str:
    return f"{target} is hit with a {element} enchantment of power {power}!"

def main():
    print("Testing spell reducer...")
    x = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(x, 'add')}")
    print(f"Product: {spell_reducer(x, 'multiply')}")
    print(f"Max: {spell_reducer(x, 'max')}")
    
    print("\nTesting memoized fibonacci...")
    print(f"Fib0: {memoized_fibonacci(0)}")
    print(f"Fib1: {memoized_fibonacci(1)}")
    print(f"Fib10: {memoized_fibonacci(10)}")
    print(f"Fib15: {memoized_fibonacci(15)}")
    
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(dispatcher(3.14))
if __name__ == "__main__":
    main()
