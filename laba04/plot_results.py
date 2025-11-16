"""
plot_results.py

Берёт results.json, строит:
- график время vs размер для выбранного типа данных (по умолчанию 'random')
- график время vs тип данных для фиксированного n (по умолчанию n=5000)
- сохраняет графики и выводит summary csv (results.csv уже есть)
"""
import json
import matplotlib.pyplot as plt
import os
from collections import defaultdict

INPUT_JSON = "results.json"

def load_results():
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def plot_time_vs_size(results, dtype='random', outname='time_vs_size.png'):
    # группируем по алгоритму
    data = defaultdict(lambda: {})
    for r in results:
        if r['type'] != dtype:
            continue
        data[r['algorithm']][r['n']] = r['time_s']
    plt.figure(figsize=(10,6))
    for alg, times in data.items():
        ns = sorted(times.keys())
        ys = [times[n] for n in ns]
        plt.plot(ns, ys, marker='o', label=alg)
    plt.xlabel('n (size)')
    plt.ylabel('time (s)')
    plt.title(f'Time vs Size on {dtype} data')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(outname)
    print(f"Saved {outname}")

def plot_time_vs_type(results, n_fixed=5000, outname='time_vs_type.png'):
    # группируем по алгоритму
    data = defaultdict(lambda: {})
    types = set()
    for r in results:
        if r['n'] != n_fixed:
            continue
        data[r['algorithm']][r['type']] = r['time_s']
        types.add(r['type'])
    types = sorted(types)
    plt.figure(figsize=(10,6))
    for alg, times in data.items():
        ys = [times.get(t, None) for t in types]
        plt.plot(types, ys, marker='o', label=alg)
    plt.xlabel('data type')
    plt.ylabel('time (s)')
    plt.title(f'Time vs Data Type (n={n_fixed})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(outname)
    print(f"Saved {outname}")

if __name__ == "__main__":
    if not os.path.exists(INPUT_JSON):
        raise FileNotFoundError("Run performance_test.py first to generate results.json")
    results = load_results()
    plot_time_vs_size(results, dtype='random', outname='time_vs_size_random.png')
    plot_time_vs_type(results, n_fixed=5000, outname='time_vs_type_n5000.png')
    print("Done.")
