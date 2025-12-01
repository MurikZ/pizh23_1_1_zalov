import random
import string
import matplotlib.pyplot as plt

from hash_functions import simple_sum, poly_hash, djb2
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import OpenAddressingHashTable

TABLE_TYPES = {
    "LinearProbing": lambda size: OpenAddressingHashTable(size, method="linear", resize=False),
    "DoubleHashing": lambda size: OpenAddressAddressingHashTable(size, method="double", resize=False)
}



# ---------- Генерация случайных строк ----------
def random_string(n=12):
    return "".join(random.choice(string.ascii_letters) for _ in range(n))


def generate_keys(count):
    return [random_string() for _ in range(count)]


# ---------- Параметры эксперимента ----------
TABLE_SIZE = 2000
LOAD_FACTORS = [0.1, 0.5, 0.7, 0.9]

HASH_FUNCTIONS = {
    "SimpleSum": simple_sum,
    "PolyHash": poly_hash,
    "DJB2": djb2
}

TABLE_TYPES = {
    "Chaining": HashTableChaining,
    "LinearProbing": HashTableLinearProbing,
    "DoubleHashing": HashTableDoubleHashing
}


# ---------- Сбор данных ----------
def measure_collisions():
    results = {}

    for hf_name, hf in HASH_FUNCTIONS.items():
        results[hf_name] = {}

        for table_name, table_cls in TABLE_TYPES.items():
            collisions_list = []

            for lf in LOAD_FACTORS:
                n_keys = int(TABLE_SIZE * lf)
                keys = generate_keys(n_keys)

                table = table_cls(TABLE_SIZE)

                for key in keys:
                    table.insert(key, 1, hf)

                collisions_list.append(table.collisions)

            results[hf_name][table_name] = collisions_list

    return results


# ---------- Построение графиков ----------
def plot_graphs(data):
    for hf_name, table_data in data.items():

        plt.figure(figsize=(10, 6))
        plt.title(f"Коллизии для разных таблиц\nХеш-функция: {hf_name}")
        plt.xlabel("Коэффициент заполнения")
        plt.ylabel("Количество коллизий")

        for table_name, collisions in table_data.items():
            plt.plot(LOAD_FACTORS, collisions, marker="o", label=table_name)

        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


# ---------- Запуск ----------
if __name__ == "__main__":
    data = measure_collisions()
    plot_graphs(data)
