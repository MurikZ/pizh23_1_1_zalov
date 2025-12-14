"""
Модуль comparison.py

Назначение:
- экспериментальное сравнение нисходящего и восходящего подходов
  динамического программирования
- измерение времени выполнения и потребления памяти
- построение и сохранение графиков зависимости времени от размера задачи

Графики сохраняются в той же директории, где расположен файл.
"""

import time
import tracemalloc
import os
import matplotlib.pyplot as plt

from dynamic_programming import fib_memo, fib_iter


def measure_time_and_memory(func, *args, repeats=5):
    times = []
    tracemalloc.start()

    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        times.append(time.perf_counter() - start)

    memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    return sum(times) / repeats, memory


# ЭКСПЕРИМЕНТ: ФИБОНАЧЧИ


def fibonacci_experiment():
    """
    Проводит эксперимент по сравнению:
    - нисходящего подхода (мемоизация)
    - восходящего подхода (табуляция)

    Строит и сохраняет график зависимости времени выполнения от n.
    """

    n_values = [5, 10, 15, 20, 25, 30, 35]
    memo_times = []
    iter_times = []

    for n in n_values:
        t_memo, _ = measure_time_and_memory(fib_memo, n)
        t_iter, _ = measure_time_and_memory(fib_iter, n)

        memo_times.append(t_memo)
        iter_times.append(t_iter)

    # ========================================================
    # ПОСТРОЕНИЕ ГРАФИКА
    # ========================================================
    plt.figure()
    plt.plot(n_values, memo_times, marker='o', label='Memoization (top-down)')
    plt.plot(n_values, iter_times, marker='o', label='Tabulation (bottom-up)')

    plt.xlabel('n (номер числа Фибоначчи)')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Сравнение подходов ДП для чисел Фибоначчи')
    plt.legend()
    plt.grid(True)

    # путь сохранения — та же папка, где лежит comparison.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'fibonacci_comparison.png')

    plt.savefig(file_path)
    plt.close()

    print(f"График сохранён: {file_path}")


# ============================================================
# ТОЧКА ВХОДА
# ============================================================

if __name__ == "__main__":
    fibonacci_experiment()
