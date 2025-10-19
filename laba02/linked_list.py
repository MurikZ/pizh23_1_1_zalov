"""
linked_list.py
Реализация простого односвязного списка с поддержкой головы и хвоста.

Классы:
- Node — элемент списка.
- LinkedList — сам список.

После каждого метода указана асимптотическая сложность.
"""

from typing import Any, Optional, Iterator


class Node:
    def __init__(self, value: Any, next: Optional["Node"] = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value!r})"


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def insert_at_start(self, value: Any) -> None:
        """Вставка в начало списка. O(1)"""
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert_at_end(self, value: Any) -> None:
        """Вставка в конец списка. O(1) при наличии хвоста"""
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def delete_from_start(self) -> Any:
        """Удаление из начала списка. O(1)"""
        if self.head is None:
            raise IndexError("delete_from_start from empty LinkedList")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return value

    def traversal(self) -> Iterator[Any]:
        """Обход всех элементов списка. O(n)"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def to_list(self) -> list:
        """Преобразовать в обычный список Python. O(n)"""
        return list(self.traversal())

    def clear(self) -> None:
        """Очистить список. O(n)"""
        self.head = None
        self.tail = None
        self._size = 0

    def __iter__(self):
        return self.traversal()

    def __repr__(self):
        return "LinkedList(" + "->".join(repr(x) for x in self.traversal()) + ")"
