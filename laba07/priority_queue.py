# priority_queue.py
"""
Простая приоритетная очередь на основе Heap (min-heap по умолчанию).
Поддерживает enqueue(item, priority) и dequeue().
"""

from typing import Any, Tuple
from heap import Heap


class PriorityQueue:
    def __init__(self, min_queue: bool = True):
        # хранить элементы как кортежи (priority, counter, item) для устойчивости
        self._counter = 0
        self._heap = Heap(is_min=min_queue, key=lambda x: x[0])

    def enqueue(self, item: Any, priority: float) -> None:
        entry = (priority, self._counter, item)
        self._counter += 1
        self._heap.insert(entry)

    def dequeue(self) -> Any:
        if self._heap.is_empty():
            raise IndexError("dequeue from empty priority queue")
        _, _, item = self._heap.extract()
        return item

    def peek(self) -> Any:
        if self._heap.is_empty():
            raise IndexError("peek from empty priority queue")
        _, _, item = self._heap.peek()
        return item

    def size(self) -> int:
        return self._heap.size()

    def is_empty(self) -> bool:
        return self._heap.is_empty()
