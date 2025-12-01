# tests.py
"""
Простейшие unit-тесты. Запуск:
python tests.py
или через pytest.
"""
import random
from heap import Heap
from heapsort import heapsort
from priority_queue import PriorityQueue


def test_heap_basic():
    h = Heap(is_min=True)
    values = [5, 1, 7, 3, 2]
    for v in values:
        h.insert(v)
    # extract order should be sorted for min-heap
    out = [h.extract() for _ in range(len(values))]
    assert out == sorted(values), f"min-heap extract order wrong: {out}"


def test_build_heap():
    arr = [random.randint(0, 100) for _ in range(20)]
    h = Heap(is_min=False)  # max-heap
    h.build_heap(arr)
    # repeatedly extract should produce descending order
    out = [h.extract() for _ in range(len(arr))]
    assert out == sorted(arr, reverse=True)


def test_heapsort():
    arr = [random.randint(-1000, 1000) for _ in range(100)]
    expected = sorted(list(arr))
    heapsort(arr)
    assert arr == expected


def test_priority_queue():
    pq = PriorityQueue(min_queue=True)
    items = [('a', 5), ('b', 1), ('c', 3)]
    for it, pr in items:
        pq.enqueue(it, pr)
    out = [pq.dequeue() for _ in range(len(items))]
    assert out == ['b', 'c', 'a']


if __name__ == "__main__":
    test_heap_basic()
    test_build_heap()
    test_heapsort()
    test_priority_queue()
    print("All tests passed.")
