"""
generate_data.py

Генерация наборов данных для тестирования сортировок:
- random
- sorted
- reversed
- almost_sorted (примерно 95% отсортировано, 5% перемешано)

Функция generate_datasets(sizes, seed) возвращает dict:
{ 'random': {n: list}, 'sorted': {n: list}, ... }
"""
import random
from typing import List, Dict

def _almost_sorted_list(n: int, fraction_sorted: float = 0.95, seed: int = None) -> List[int]:
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    # оставляем первые int(fraction_sorted*n) элементов на месте, перемешиваем остальные
    k = int(n * fraction_sorted)
    tail = arr[k:]
    random.shuffle(tail)
    return arr[:k] + tail

def generate_datasets(sizes = [100, 1000, 5000, 10000], seed: int = 42) -> Dict[str, Dict[int, List[int]]]:
    random.seed(seed)
    datasets = {'random': {}, 'sorted': {}, 'reversed': {}, 'almost_sorted': {}}
    for n in sizes:
        base = [random.randint(0, n*10) for _ in range(n)]
        datasets['random'][n] = base.copy()
        datasets['sorted'][n] = sorted(base)
        datasets['reversed'][n] = sorted(base, reverse=True)
        # almost_sorted: take sorted array and shuffle small part
        sorted_arr = sorted(base)
        k = max(1, int(n * 0.05))  # 5% элементов перемешаем
        # swap k pairs at random positions
        almost = sorted_arr.copy()
        for _ in range(k):
            i = random.randrange(n)
            j = random.randrange(n)
            almost[i], almost[j] = almost[j], almost[i]
        datasets['almost_sorted'][n] = almost
    return datasets

if __name__ == "__main__":
    # небольшой самотест
    d = generate_datasets([100, 1000], seed=1)
    for t in d:
        for n in d[t]:
            print(t, n, len(d[t][n]))
