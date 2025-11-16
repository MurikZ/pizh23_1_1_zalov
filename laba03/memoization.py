"""
memoization.py
Мемоизированная версия вычисления чисел Фибоначчи
и инструмент сравнения времени работы + построение графиков.
"""

from functools import lru_cache
import time
import matplotlib.pyplot as plt

call_count = 0


# -------------------------------
#   НАИВНАЯ РЕКУРСИЯ
# -------------------------------
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


# -------------------------------
#   МЕМОИЗИРОВАННАЯ РЕАЛИЗАЦИЯ
# -------------------------------
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


# -------------------------------
#   ИЗМЕРЕНИЕ ВРЕМЕНИ
# -------------------------------
def measure(func, n: int):
    """Возвращает (результат, время, число вызовов)."""
    global call_count
    reset_count()
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start, call_count


# -------------------------------
#   ПОСТРОЕНИЕ ГРАФИКА
# -------------------------------
def plot_times(ns, naive_times, memo_times):
    plt.figure(figsize=(10, 6))
    plt.plot(ns, naive_times, marker='o', label='Наивный')
    plt.plot(ns, memo_times, marker='o', label='Мемоизация')
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение времени вычисления Фибоначчи")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("fib_graph.png")
    print("График сохранён в файл fib_graph.png")


# -------------------------------
#   ОСНОВНОЙ ЗАПУСК
# -------------------------------
if __name__ == "__main__":

    print("\n=== Сравнение для n = 35 ===")

    # ---- Наивный ----
    naive_res, naive_time, naive_calls = measure(fib_naive_count, 35)
    print(f"Наивный результат: {naive_res}")
    print(f"Время работы: {naive_time:.5f} сек")
    print(f"Количество рекурсивных вызовов: {naive_calls}")

    # ---- Мемоизированный ----
    fib_memoized.cache_clear()
    memo_res, memo_time, memo_calls = measure(fib_memoized, 35)
    print(f"\nМемоизированный результат: {memo_res}")
    print(f"Время работы: {memo_time:.5f} сек")
    print(f"Количество рекурсивных вызовов: {memo_calls}")

    # ---- Построение графика для разных n ----
    print("\n=== Построение графика ===")
    test_ns = [5, 10, 15, 20, 25, 30, 35]
    naive_times = []
    memo_times = []

    for n in test_ns:
        print(f"n={n}: замеры...")
        _, t_naive, _ = measure(fib_naive_count, n)
        fib_memoized.cache_clear()
        _, t_memo, _ = measure(fib_memoized, n)
        naive_times.append(t_naive)
        memo_times.append(t_memo)

    plot_times(test_ns, naive_times, memo_times)
    print("\nГотово!")
