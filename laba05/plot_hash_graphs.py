"""
plot_hash_graphs.py
Упрощённая визуализация ХЕШ-ТАБЛИЦ без использования JSON.

Строит два графика:
1) Время операций от коэффициента заполнения
2) Количество коллизий для разных хеш-функций
"""

import matplotlib.pyplot as plt
import numpy as np



def plot_time_vs_load(outname="time_vs_load.png"):
    load = np.linspace(0.1, 0.95, 20)

    # искусственные модели поведения
    chaining = 0.5 + load * 0.4
    linear = 0.3 + (load ** 4) * 10      # взрыв нагрузки
    double = 0.25 + (load ** 3) * 5      # растёт, но легче

    plt.figure(figsize=(10, 6))
    plt.plot(load, chaining, marker="o", label="Chaining (цепочки)")
    plt.plot(load, linear, marker="s", label="Linear probing")
    plt.plot(load, double, marker="^", label="Double hashing")

    plt.xlabel("Коэффициент заполнения (load factor)")
    plt.ylabel("Время операции (отн. ед.)")
    plt.title("Зависимость времени операций от коэффициента заполнения")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(outname)
    plt.close()

    print(f"График сохранён как {outname}")




def plot_hash_collision_hist(outname="hash_collision_hist.png"):
    functions = ["SimpleHash", "PolynomialHash", "DJB2"]
    collisions = [1200, 450, 180]  # искусственные данные

    plt.figure(figsize=(10, 6))
    plt.bar(functions, collisions)

    plt.xlabel("Хеш-функция")
    plt.ylabel("Количество коллизий")
    plt.title("Сравнение количества коллизий хеш-функций")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(outname)
    plt.close()

    print(f"Гистограмма сохранена как {outname}")


if __name__ == "__main__":
    plot_time_vs_load("time_vs_load.png")
    plot_hash_collision_hist("hash_collision_hist.png")
    print("Готово.")
