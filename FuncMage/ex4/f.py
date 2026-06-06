
import functools
from typing import  Callable
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        x = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return x
    return enhanced_fn


@spell_timer
def fireball():
    """هذه دالة لرمي كرة نار"""
    pass

print(fireball.__name__) 
# بدون wraps سيطبع: enhanced_fn
# مع wraps سيطبع: fireball