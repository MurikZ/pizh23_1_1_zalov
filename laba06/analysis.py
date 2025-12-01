from __future__ import annotations
import random
import time
from typing import List
import matplotlib.pyplot as plt
import os
from binary_search_tree import BinarySearchTree

# Создаём папку для графиков
os.makedirs("plots", exist_ok=True)


def build_balanced_from_list(values: List[int]) -> BinarySearchTree:
    bst = BinarySearchTree()
    for v in random.sample(values, len(values)):
        bst.insert(v)
    return bst


def build_degenerate_from_list(values: List[int]) -> BinarySearchTree:
    bst = BinarySearchTree()
    for v in sorted(values):
        bst.insert(v)
    return bst


def time_searches(bst: BinarySearchTree, queries: List[int]) -> float:
    start = time.perf_counter()
    for q in queries:
        bst.search(q)
    end = time.perf_counter()
    return end - start


def run_experiment(max_n: int = 2000, step: int = 200, searches: int = 1000) -> None:
    sizes = list(range(step, max_n + 1, step))
    balanced_times = []
    degenerate_times = []

    for n in sizes:
        values = list(range(n))
        queries = [random.randrange(0, n) for _ in range(searches)]

        balanced = build_balanced_from_list(values)
        degenerate = build_degenerate_from_list(values)

        t_bal = time_searches(balanced, queries)
        t_deg = time_searches(degenerate, queries)

        balanced_times.append(t_bal)
        degenerate_times.append(t_deg)

        print(f"n={n}: balanced={t_bal:.6f}s, degenerate={t_deg:.6f}s")

    plt.figure(figsize=(8, 4))
    plt.plot(sizes, balanced_times, label="Сбалансированное дерево")
    plt.plot(sizes, degenerate_times, label="Вырожденное дерево")
    plt.xlabel("Количество элементов n")
    plt.ylabel(f"Время {searches} поисков (сек)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Сохраняем в ПАПКУ ./plots/
    plt.savefig("bst_timing.png")
    plt.close()
    print("График сохранён в plots/bst_timing.png")

if __name__ == "__main__":
    run_experiment()