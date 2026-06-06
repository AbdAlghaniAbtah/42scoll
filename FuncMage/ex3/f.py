import functools
import time

# الدالة الأولى (مع كاش)
@functools.lru_cache(maxsize=None)
def memoized_fib(n: int) -> int:
    if n < 2:
        return n
    return memoized_fib(n - 1) + memoized_fib(n - 2)

# الدالة الثانية (بدون كاش - أصلية)
def slow_fib(n: int) -> int:
    if n < 2:
        return n
    return slow_fib(n - 1) + slow_fib(n - 2)

def main():
    n = 37 # جرب رقماً كبيراً لتشعر بالفرق
    print(f"Testing memoized_fib({n})...")
    start = time.time()
    print(f"Result: {memoized_fib(n)}")
    print(f"Time: {time.time() - start:.5f} seconds")
    # 1. اختبار الدالة البطيئة
    start = time.time()
    print(f"Result: {slow_fib(n)}")
    print(f"Time: {time.time() - start:.5f} seconds")

    # 2. اختبار الدالة مع الكاش


if __name__ == "__main__":
    main()