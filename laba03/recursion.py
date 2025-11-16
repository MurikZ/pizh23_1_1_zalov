"""
recursion.py
Реализация базовых рекурсивных алгоритмов:
- factorial(n)
- fib(n)
- pow_fast(a, n)
"""

def factorial(n: int) -> int:
    """
    Возвращает n! (факториал числа n).
    Временная сложность: O(n)
    Глубина рекурсии: n
    """
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fib(n: int) -> int:
    """
    Наивная рекурсивная функция вычисления n-го числа Фибоначчи.
    Временная сложность: O(φ^n)
    Глубина рекурсии: n
    """
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def pow_fast(a: float, n: int) -> float:
    """
    Быстрое возведение a в степень n (через степень двойки).
    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if n < 0:
        return 1.0 / pow_fast(a, -n)
    if n == 0:
        return 1.0
    if n == 1:
        return a
    half = pow_fast(a, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * a
