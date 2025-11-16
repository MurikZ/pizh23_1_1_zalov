"""
memoization.py
Мемоизированная версия вычисления чисел Фибоначчи
и инструмент сравнения времени работы.
"""

from functools import lru_cache

call_count = 0


def fib_naive_count(n: int) -> int:
    """Наивная рекурсивная версия с подсчётом вызовов."""
    global call_count
    call_count += 1
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_naive_count(n - 1) + fib_naive_count(n - 2)


def reset_count():
    """Сброс счётчика вызовов."""
    global call_count
    call_count = 0


@lru_cache(maxsize=None)
def fib_memoized(n: int) -> int:
    """Мемоизированная версия вычисления Фибоначчи."""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_memoized(n - 1) + fib_memoized(n - 2)
