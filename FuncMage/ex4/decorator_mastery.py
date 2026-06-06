import functools
from typing import  Callable
import time

def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        time.sleep(0.5)
        x = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return x
    return enhanced_fn

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(self, power: int, *args, **kwargs):
            if power >= min_power:
                return func(self, power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    if attempts < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempts}/{max_attempts})")
                    else:
                        print(f"Spell casting failed after {max_attempts} attempts")
            return "Spell failed" 
        return wrapper
    return decorator
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not name or len(name) < 3 or not name.isalpha():
            return False
        return True
    @power_validator(min_power=50)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Spell '{spell_name}' cast with power {power}!"

def main():
    print("Testing spell timer...")
    @spell_timer
    def fireball():
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    @retry_spell(3)
    def failing_spell():
        raise Exception("Failed")
    print(failing_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Merlin"))
    print(guild.validate_mage_name("Jo"))
    
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Fireball"))

if __name__ == "__main__":
    main()