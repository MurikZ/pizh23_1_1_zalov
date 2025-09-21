import time
import matplotlib.pyplot as plt

# -----------------------------
# ЛИНЕЙНЫЙ ПОИСК
# -----------------------------
def linear_search(arr, target):  # O(1)
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)
# Общая сложность: O(n)


# -----------------------------
# БИНАРНЫЙ ПОИСК
# -----------------------------
def binary_search(arr, target):  # O(1)
    left, right = 0, len(arr) - 1  # O(1)
    while left <= right:  # O(log n)
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:  # O(1)
            return mid  # O(1)
        elif arr[mid] < target:  # O(1)
            left = mid + 1  # O(1)
        else:  # O(1)
            right = mid - 1  # O(1)
    return -1  # O(1)
# Общая сложность: O(log n)


# -----------------------------
# ФУНКЦИЯ ДЛЯ ЗАМЕРОВ ВРЕМЕНИ
# -----------------------------
def measure_time(func, arr, target, repeats=5):  # O(1)
    start = time.perf_counter()  # O(1)
    for _ in range(repeats):  # O(repeats)
        func(arr, target)  # O(T(n)) — зависит от алгоритма (O(n) или O(log n))
    end = time.perf_counter()  # O(1)
    return (end - start) / repeats  # O(1)
# Общая сложность: O(repeats * T(n)), где T(n) — сложность алгоритма поиска


# -----------------------------
# ГЛАВНАЯ ПРОГРАММА
# -----------------------------
def main():  # O(1)
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]  # O(1)
    linear_times = []  # O(1)
    binary_times = []  # O(1)

    for size in sizes:  # O(k), где k = количество размеров
        arr = list(range(size))  # O(n)
        targets = [arr[0], arr[size // 2], arr[-1], -1]  # O(1)

        # замер линейного поиска
        total_linear = 0  # O(1)
        for t in targets:  # O(m), m = 4
            total_linear += measure_time(linear_search, arr, t)  # O(n)
        linear_times.append(total_linear / len(targets))  # O(1)

        # замер бинарного поиска
        total_binary = 0  # O(1)
        for t in targets:  # O(m), m = 4
            total_binary += measure_time(binary_search, arr, t)  # O(log n)
        binary_times.append(total_binary / len(targets))  # O(1)

        print(f"Размер: {size}, Linear avg: {linear_times[-1]:.6f}, Binary avg: {binary_times[-1]:.6f}")  # O(1)

    # График 1: линейный масштаб
    plt.figure(figsize=(10, 6))  # O(1)
    plt.plot(sizes, linear_times, label="Линейный поиск O(n)", marker="o")  # O(k)
    plt.plot(sizes, binary_times, label="Бинарный поиск O(log n)", marker="o")  # O(k)
    plt.xlabel("Размер массива")  # O(1)
    plt.ylabel("Среднее время (сек)")  # O(1)
    plt.title("Сравнение линейного и бинарного поиска")  # O(1)
    plt.legend()  # O(1)
    plt.grid(True)  # O(1)
    plt.show()  # O(1)

    # График 2: логарифмический масштаб по Y
    plt.figure(figsize=(10, 6))  # O(1)
    plt.plot(sizes, linear_times, label="Линейный поиск O(n)", marker="o")  # O(k)
    plt.plot(sizes, binary_times, label="Бинарный поиск O(log n)", marker="o")  # O(k)
    plt.xlabel("Размер массива")  # O(1)
    plt.ylabel("Среднее время (сек)")  # O(1)
    plt.title("Сравнение в логарифмическом масштабе")  # O(1)
    plt.yscale("log")  # O(1)
    plt.legend()  # O(1)
    plt.grid(True, which="both")  # O(1)
    plt.show()  # O(1)


if __name__ == "__main__":  # O(1)
    main()  # O(k * (n + log n)) примерно
