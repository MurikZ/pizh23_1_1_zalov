import random
import time
import matplotlib.pyplot as plt

# -----------------------------
# ЛИНЕЙНЫЙ ПОИСК
# -----------------------------
def linear_search(arr, target):
    # O(n) - в худшем случае проверим все элементы
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)
# Общая сложность: O(n)


# -----------------------------
# БИНАРНЫЙ ПОИСК
# -----------------------------
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # O(1)
    while left <= right:  # O(log n)
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:  # O(1)
            return mid  # O(1)
        elif arr[mid] < target:  # O(1)
            left = mid + 1  # O(1)
        else:
            right = mid - 1  # O(1)
    return -1  # O(1)
# Общая сложность: O(log n)


# -----------------------------
# ФУНКЦИЯ ДЛЯ ЗАМЕРОВ ВРЕМЕНИ
# -----------------------------
def measure_time(func, arr, target, repeats=5):
    start = time.time()
    for _ in range(repeats):
        func(arr, target)
    end = time.time()
    return (end - start) / repeats


# -----------------------------
# ГЛАВНАЯ ПРОГРАММА
# -----------------------------
def main():
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    linear_times = []
    binary_times = []

    for size in sizes:
        arr = list(range(size))  # отсортированный массив
        targets = [arr[0], arr[size // 2], arr[-1], -1]  # первый, середина, последний, отсутствующий

        # замер линейного поиска
        total_linear = 0
        for t in targets:
            total_linear += measure_time(linear_search, arr, t)
        linear_times.append(total_linear / len(targets))

        # замер бинарного поиска
        total_binary = 0
        for t in targets:
            total_binary += measure_time(binary_search, arr, t)
        binary_times.append(total_binary / len(targets))

        print(f"Размер: {size}, Linear avg: {linear_times[-1]:.6f}, Binary avg: {binary_times[-1]:.6f}")

    # График 1: линейный масштаб
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, label="Линейный поиск O(n)", marker="o")
    plt.plot(sizes, binary_times, label="Бинарный поиск O(log n)", marker="o")
    plt.xlabel("Размер массива")
    plt.ylabel("Среднее время (сек)")
    plt.title("Сравнение линейного и бинарного поиска")
    plt.legend()
    plt.grid(True)
    plt.show()

    # График 2: логарифмический масштаб по Y
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, label="Линейный поиск O(n)", marker="o")
    plt.plot(sizes, binary_times, label="Бинарный поиск O(log n)", marker="o")
    plt.xlabel("Размер массива")
    plt.ylabel("Среднее время (сек)")
    plt.title("Сравнение в логарифмическом масштабе")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both")
    plt.show()


if __name__ == "__main__":
    main()