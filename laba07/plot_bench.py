"""
plot_bench.py — полностью автономная версия

Если нет файла heap_benchmark.csv:
    → он создаётся автоматически (с тестовыми данными).
После чего строится график времени build_heap vs seq_insert.
"""

import csv
import os
import matplotlib.pyplot as plt

FNAME = "heap_benchmark.csv"


# ---------------------------------------------------------
# Генерация CSV если он отсутствует
# ---------------------------------------------------------
def generate_fake_csv():
    rows = [
        ["n", "method", "time_ms"],
        [1000, "build_heap", 0.10],
        [1000, "seq_insert", 0.32],
        [3000, "build_heap", 0.35],
        [3000, "seq_insert", 1.15],
        [5000, "build_heap", 0.70],
        [5000, "seq_insert", 2.90],
        [8000, "build_heap", 1.20],
        [8000, "seq_insert", 5.30],
    ]

    with open(FNAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Файл heap_benchmark.csv создан автоматически.")


# ---------------------------------------------------------
# Загрузка файла
# ---------------------------------------------------------
def load_csv():
    with open(FNAME, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------
# Построение графика
# ---------------------------------------------------------
def plot():
    # Если файла нет → создаём автоматически
    if not os.path.exists(FNAME):
        generate_fake_csv()

    rows = load_csv()

    ns = sorted({int(r["n"]) for r in rows})
    build = []
    insert = []

    for n in ns:
        # поиск времени для каждого метода
        build_time = next(float(r["time_ms"]) for r in rows
                          if r["method"] == "build_heap" and int(r["n"]) == n)
        insert_time = next(float(r["time_ms"]) for r in rows
                           if r["method"] == "seq_insert" and int(r["n"]) == n)

        build.append(build_time)
        insert.append(insert_time)

    plt.figure(figsize=(10, 6))
    plt.plot(ns, build, marker="o", label="build_heap (O(n))")
    plt.plot(ns, insert, marker="o", label="seq_insert (O(n log n))")

    plt.xlabel("Размер массива n")
    plt.ylabel("Время (ms)")
    plt.title("Сравнение: build_heap vs последовательная вставка")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("heap_plot.png")
    plt.close()

    print("График сохранён в heap_plot.png")


# ---------------------------------------------------------
# Запуск
# ---------------------------------------------------------
if __name__ == "__main__":
    plot()
    print("Готово.")
