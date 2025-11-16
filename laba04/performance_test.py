"""
performance_test.py

Измерение времени выполнения каждого алгоритма сортировки
на разных типах данных и размерах. Использует timeit.repeat.

Сохраняет результаты в results.json и results.csv.
"""
import timeit
import json
import csv
from generate_data import generate_datasets
import sort
import os

# настройки
SIZES = [100, 1000, 5000, 10000]
TYPES = ['random', 'sorted', 'reversed', 'almost_sorted']
ALGORITHMS = {
    'bubble_sort': sort.bubble_sort,
    'selection_sort': sort.selection_sort,
    'insertion_sort': sort.insertion_sort,
    'merge_sort': sort.merge_sort,
    'quick_sort': sort.quick_sort,
}
REPEATS = 3   # количество повторов времени (timeit.repeat)
NUMBER = 1    # запуск функции NUMBER раз в одном измерении (мы используем NUMBER=1 и повторяем REPEATS раз)
OUTPUT_JSON = "results.json"
OUTPUT_CSV = "results.csv"

def measure_one(func, arr):
    """
    Измеряет время выполнения func(arr_copy) используя timeit.repeat с callable.
    Возвращает среднее время из REPEATS запусков.
    """
    # timeit.repeat принимает callable как stmt начиная с Python 3.5+
    tlist = timeit.repeat(stmt=lambda: func(arr.copy()), repeat=REPEATS, number=NUMBER)
    return sum(tlist) / len(tlist)

def main():
    datasets = generate_datasets(SIZES, seed=123)
    results = []
    total_runs = len(SIZES) * len(TYPES) * len(ALGORITHMS)
    run_i = 0
    for dtype in TYPES:
        for n in SIZES:
            arr = datasets[dtype][n]
            for name, func in ALGORITHMS.items():
                run_i += 1
                print(f"[{run_i}/{total_runs}] {name} on {dtype} n={n} ...", end=" ")
                # корректность: функция должна возвращать отсортированный список
                sorted_ref = sorted(arr)
                res = func(arr.copy())
                if res != sorted_ref:
                    print("ERROR: incorrect result!")
                    raise RuntimeError(f"{name} failed to sort {dtype} n={n}")
                # измерение
                t = measure_one(func, arr)
                print(f"done, time={t:.6f}s")
                results.append({
                    'algorithm': name,
                    'type': dtype,
                    'n': n,
                    'time_s': t
                })

    # сохраняем в JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    # сохраняем в CSV (сводная таблица)
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['algorithm','type','n','time_s'])
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    print(f"Saved results to {OUTPUT_JSON} and {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
