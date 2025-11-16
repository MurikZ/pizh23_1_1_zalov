"""
sorts.py

Реализация 5 алгоритмов сортировки:
- bubble_sort
- selection_sort
- insertion_sort
- merge_sort
- quick_sort

Каждая функция возвращает новый отсортированный список (не мутирует исходный).
Комментарии указывают временные и пространственные сложности.
"""

from typing import List
import random

# 1) Bubble Sort
def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort (обменная сортировка).

    Временная сложность:
      - худший: O(n^2)
      - средний: O(n^2)
      - лучший: O(n) (если массив уже отсортирован и реализована проверка на отсутствие обменов)
    Пространственная сложность: O(1) дополнительной памяти (in-place).

    Примечание: реализована версия, работающая на копии массива (возвращает новый список).
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


# 2) Selection Sort
def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort (поиск минимума и перестановка).

    Временная сложность:
      - худший: O(n^2)
      - средний: O(n^2)
      - лучший: O(n^2)
    Пространственная сложность: O(1) дополнительной памяти (in-place).
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


# 3) Insertion Sort
def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort (вставками).

    Временная сложность:
      - худший: O(n^2)
      - средний: O(n^2)
      - лучший: O(n) (массив уже отсортирован)
    Пространственная сложность: O(1) дополнительной памяти (in-place) — тут возвращаем копию.
    """
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# 4) Merge Sort
def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort (сортировка слиянием, рекурсивная).

    Временная сложность:
      - худший: O(n log n)
      - средний: O(n log n)
      - лучший: O(n log n)
    Пространственная сложность: O(n) дополнительной памяти (для слияния).
    """
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # слияние
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])
    return res


# 5) Quick Sort (рандомизированный выбор опорного элемента)
def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort (быстрая сортировка, рекурсивная, рандомизированная опора).

    Временная сложность:
      - худший: O(n^2) (плохой выбор опорного элемента, например, уже отсортированный массив и фиксация опоры)
      - средний: O(n log n)
      - лучший: O(n log n)
    Пространственная сложность: O(log n) в среднем для рекурсивного стека (в худшем O(n)).

    Примечание: рандомизация (случайный pivot) уменьшает шанс худшего случая на типичных данных.
    """
    if len(arr) <= 1:
        return arr.copy()
    a = arr.copy()
    pivot = random.choice(a)
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
