"""
performance_analysis.py
Сравнение производительности встроенных структур данных (list, deque)
и пользовательского LinkedList.
"""

import timeit
from collections import deque
import matplotlib.pyplot as plt
from linked_list import LinkedList
from pathlib import Path

OUT_DIR = Path(".")
OUT_DIR.mkdir(exist_ok=True)


def time_insert_at_start_list(n, repetitions=3):
    def single_run():
        lst = []
        for i in range(n):
            lst.insert(0, i)
    t = timeit.timeit(single_run, number=repetitions)
    return t / repetitions


def time_insert_at_start_linkedlist(n, repetitions=3):
    def single_run():
        ll = LinkedList()
        for i in range(n):
            ll.insert_at_start(i)
    t = timeit.timeit(single_run, number=repetitions)
    return t / repetitions


def time_pop0_list(n, repetitions=3):
    def single_run():
        lst = list(range(n))
        for _ in range(n):
            lst.pop(0)
    t = timeit.timeit(single_run, number=repetitions)
    return t / repetitions


def time_popleft_deque(n, repetitions=3):
    def single_run():
        dq = deque(range(n))
        for _ in range(n):
            dq.popleft()
    t = timeit.timeit(single_run, number=repetitions)
    return t / repetitions


def run_benchmarks(sizes):
    results = {
        "size": [],
        "list_insert0": [],
        "linkedlist_insert_start": [],
        "list_pop0": [],
        "deque_popleft": []
    }
    for n in sizes:
        print(f"Benchmarking n={n}...")
        results["size"].append(n)
        results["list_insert0"].append(time_insert_at_start_list(n))
        results["linkedlist_insert_start"].append(time_insert_at_start_linkedlist(n))
        results["list_pop0"].append(time_pop0_list(n))
        results["deque_popleft"].append(time_popleft_deque(n))
    return results


def plot_results(results):
    sizes = results["size"]

    # 1️⃣ Вставка в начало (list vs LinkedList)
    plt.figure()
    plt.plot(sizes, results["list_insert0"], marker="o", label="list.insert(0, x)")
    plt.plot(sizes, results["linkedlist_insert_start"], marker="o", label="LinkedList.insert_at_start(x)")
    plt.xlabel("Количество вставок (n)")
    plt.ylabel("Время (секунды)")
    plt.title("Вставка в начало: list vs LinkedList")
    plt.legend()
    plt.grid(True)
    plt.savefig(OUT_DIR / "insert_at_start_comparison.png")

    # 2️⃣ Удаление с начала (list vs deque)
    plt.figure()
    plt.plot(sizes, results["list_pop0"], marker="o", label="list.pop(0)")
    plt.plot(sizes, results["deque_popleft"], marker="o", label="deque.popleft()")
    plt.xlabel("Количество удалений (n)")
    plt.ylabel("Время (секунды)")
    plt.title("Удаление с начала: list vs deque")
    plt.legend()
    plt.grid(True)
    plt.savefig(OUT_DIR / "pop_from_start_comparison.png")


def main():
    sizes = [100, 500, 1000, 2000, 4000]
    results = run_benchmarks(sizes)
    plot_results(results)
    for i, n in enumerate(results["size"]):
        print(f"n={n}: list.insert0={results['list_insert0'][i]:.6f}s | "
              f"LinkedList.insert={results['linkedlist_insert_start'][i]:.6f}s | "
              f"list.pop0={results['list_pop0'][i]:.6f}s | deque.popleft={results['deque_popleft'][i]:.6f}s")


if __name__ == "__main__":
    main()
