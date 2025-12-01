# heap.py
"""
Универсальная реализация кучи на основе массива.
Класс Heap поддерживает min-кучу (is_min=True) и max-кучу (is_min=False).

Основные методы:
- insert(value)         O(log n) амортизированно
- extract()             O(log n)
- peek()                O(1)
- build_heap(array)     O(n)
- _sift_up(idx)         O(log n)
- _sift_down(idx)       O(log n)
- to_tree_string()      текстовое представление кучи (для небольших n)
"""

from typing import List, Optional, Callable, Any


class Heap:
    def __init__(self, is_min: bool = True, key: Optional[Callable[[Any], Any]] = None):
        """
        :param is_min: True для min-heap, False для max-heap
        :param key: необязательная функция ключа (как в sorted)
        """
        self.data: List[Any] = []
        self.is_min = is_min
        self.key = key or (lambda x: x)


    def _compare(self, a, b) -> bool:
        """Возвращает True, если a имеет более высокий приоритет чем b (для вставок/перемещений).
        Для min-кучи это a < b, для max-кучи — a > b (по key).
        """
        ka = self.key(a)
        kb = self.key(b)
        return ka < kb if self.is_min else ka > kb

    def _sift_up(self, idx: int) -> None:
        """
        Всплытие элемента с индекса idx вверх до корректной позиции.
        Сложность: O(log n)
        """
        while idx > 0:
            parent = (idx - 1) // 2
            if self._compare(self.data[idx], self.data[parent]):
                self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx: int) -> None:
        """
        Погружение элемента с индекса idx вниз до корректной позиции.
        Сложность: O(log n)
        """
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            chosen = idx

            if left < n and self._compare(self.data[left], self.data[chosen]):
                chosen = left
            if right < n and self._compare(self.data[right], self.data[chosen]):
                chosen = right

            if chosen == idx:
                break
            self.data[idx], self.data[chosen] = self.data[chosen], self.data[idx]
            idx = chosen


    def insert(self, value: Any) -> None:
        """
        Вставка value в кучу.
        Сложность: O(log n)
        """
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def peek(self) -> Any:
        """
        Просмотр корня кучи (min или max) без удаления.
        Сложность: O(1)
        """
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def extract(self) -> Any:
        """
        Удаление и возвращение корня.
        Сложность: O(log n)
        """
        if not self.data:
            raise IndexError("extract from empty heap")
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return root

    def size(self) -> int:
        return len(self.data)

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def build_heap(self, array: List[Any]) -> None:
        """
        Построение кучи из массива за O(n) методом "heapify":
        - копируем данные
        - вызываем sift_down для всех внутренних узлов справа-налево
        Сложность: O(n)
        """
        self.data = list(array)
        # последний ненулевой индекс родителя:
        n = len(self.data)
        if n <= 1:
            return
        for i in range((n // 2) - 1, -1, -1):
            self._sift_down(i)


    def to_list(self) -> List[Any]:
        return list(self.data)

    def to_tree_string(self, max_width: int = 80) -> str:
        """
        Текстовое представление кучи как уровневого дерева (не для больших n).
        Полезно для демонстраций.
        """
        if not self.data:
            return "<empty heap>"
        lines = []
        level = 0
        n = len(self.data)
        i = 0
        while i < n:
            count = 2 ** level
            level_items = self.data[i:i + count]
            lines.append(" ".join(str(x) for x in level_items))
            i += count
            level += 1
        return "\n".join(lines)

    def __repr__(self):
        return f"Heap(is_min={self.is_min}, size={len(self.data)})"
