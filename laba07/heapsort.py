# heapsort.py
"""
In-place heapsort (сортировка кучей).
Реализует сортировку массива на месте, используя max-heap.
Сложность: O(n log n) во всех случаях (худший/средний/лучший).
Память: O(1) (in-place).
"""

from typing import List


def heapsort(arr: List) -> None:
    """
    Сортирует arr по возрастанию на месте.
    Подход: сначала построим max-heap in-place (heapify), затем повторно извлекаем максимум,
    перемещая его в конец массива, уменьшая границу heap_size.
    """
    n = len(arr)
    # heapify (макс-куча): для удобства используем сравнение > (поведение по умолчанию)
    # делаем "sift_down" inline
    def sift_down(a: List, start: int, end: int) -> None:
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            # выберем больший из детей
            if child + 1 <= end and a[child] < a[child + 1]:
                child += 1
            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                break

    # build max heap
    for i in range((n // 2) - 1, -1, -1):
        sift_down(arr, i, n - 1)

    # сортировка: каждый раз перемещаем максимум в конец и уменьшаем heap
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
