import time
import random
import matplotlib.pyplot as plt
import os
from greedy_algorithms import fractional_knapsack, huffman_coding


def knapsack_bruteforce(items, capacity):
    n = len(items)
    best = 0

    for mask in range(1 << n):
        total_weight = 0
        total_value = 0

        for i in range(n):
            if mask & (1 << i):
                total_value += items[i][0]
                total_weight += items[i][1]

        if total_weight <= capacity:
            best = max(best, total_value)

    return best


def compare_knapsack():
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50

    greedy_result = fractional_knapsack(items, capacity)
    exact_result = knapsack_bruteforce(items, capacity)

    print("Greedy (fractional):", greedy_result)
    print("Exact (0-1):", exact_result)


def huffman_experiment():
    sizes = [100, 500, 1000, 2000, 5000]
    times = []

    for n in sizes:
        frequencies = {chr(65 + i): random.randint(1, 100) for i in range(n)}
        start = time.time()
        huffman_coding(frequencies)
        times.append(time.time() - start)

    return sizes, times


def save_plot(sizes, times):
    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Размер входных данных (количество символов)")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Время работы алгоритма Хаффмана")
    plt.grid(True)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "huffman_time.png")

    plt.savefig(file_path)
    plt.close()

    print(f"График сохранён: {file_path}")


if __name__ == "__main__":
    compare_knapsack()
    sizes, times = huffman_experiment()
    save_plot(sizes, times)
