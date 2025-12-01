"""
binary_search_tree.py

Реализация бинарного дерева поиска (Binary Search Tree, BST) на основе узлов.
Содержит операции вставки, поиска, удаления, вычисления высоты, проверки корректности BST,
а также вспомогательные методы (поиск минимума, максимума, визуализация).

Каждая функция сопровождается описанием временной сложности в худшем и среднем случае.
"""

from __future__ import annotations
from typing import Optional, Any, List


class TreeNode:
    """
    Узел бинарного дерева поиска.

    Атрибуты:
        value (Any): Значение, хранимое в узле. Должно поддерживать операции сравнения.
        left (TreeNode | None): Левый потомок, содержащий элементы < value.
        right (TreeNode | None): Правый потомок, содержащий элементы > value.

    Примечание:
        В данной реализации узел не хранит ссылку на родителя.
    """

    def __init__(self, value: Any):
        """
        Инициализирует узел дерева.

        Args:
            value: Значение, помещаемое в узел.
        """
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        """
        Возвращает строковое представление узла.
        """
        return f"TreeNode({self.value!r})"


class BinarySearchTree:
    """
    Класс бинарного дерева поиска (BST).

    Основные свойства BST:
        - Все значения в левом поддереве узла меньше его значения.
        - Все значения в правом поддереве больше его значения.
        - Каждое поддерево также является BST.
    """

    def __init__(self):
        """Создаёт пустое дерево."""
        self.root: Optional[TreeNode] = None

    def insert(self, value: Any) -> None:
        """
        Вставляет новое значение в дерево.

        Алгоритм:
            - Спускаемся по дереву, сравнивая значение с текущим узлом.
            - Если значение меньше — идём в левое поддерево.
            - Если больше — в правое.
            - Если достигнут пустой узел — вставляем новый.

        Args:
            value: Добавляемое значение.

        Сложность:
            Средняя: O(log n) — если дерево сбалансировано.
            Худшая: O(n) — если дерево вырождено в цепочку.
        """
        if self.root is None:
            self.root = TreeNode(value)
            return

        node = self.root
        while True:
            if value == node.value:
                # Дубликаты не вставляются
                return
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    return
                node = node.left
            else:  # value > node.value
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                node = node.right

    def search(self, value: Any) -> Optional[TreeNode]:
        """
        Ищет узел с данным значением.

        Args:
            value: Значение, которое нужно найти.

        Returns:
            TreeNode или None.

        Сложность:
            Средняя: O(log n)
            Худшая: O(n)
        """
        node = self.root
        while node is not None:
            if value == node.value:
                return node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return None


    def find_min(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Находит минимальный элемент (самый левый узел) в поддереве.

        Args:
            node: Корень поддерева.

        Returns:
            Узел с минимальным значением или None.

        Сложность: O(h), где h — высота поддерева.
        """
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def find_max(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Находит максимальный элемент (самый правый узел) в поддереве.

        Args:
            node: Корень поддерева.

        Returns:
            Узел с максимальным значением или None.

        Сложность: O(h)
        """
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node

    def delete(self, value: Any) -> None:
        """
        Удаляет узел с данным значением, если он существует.

        Случаи удаления:
            1. Узел — лист → удаляется сразу.
            2. Один потомок → заменяется потомком.
            3. Два потомка → заменяется in-order преемником.

        Args:
            value: Значение для удаления.

        Сложность:
            Средняя: O(log n)
            Худшая: O(n)
        """

        def _delete(node: Optional[TreeNode], val: Any) -> Optional[TreeNode]:
            if node is None:
                return None

            if val < node.value:
                node.left = _delete(node.left, val)
                return node
            if val > node.value:
                node.right = _delete(node.right, val)
                return node

            # 1. Лист
            if node.left is None and node.right is None:
                return None

            # 2. Один ребёнок
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # 3. Два ребёнка — заменяем преемником
            successor = self.find_min(node.right)
            node.value = successor.value
            node.right = _delete(node.right, successor.value)
            return node

        self.root = _delete(self.root, value)


    def height(self, node: Optional[TreeNode] = None) -> int:
        """
        Вычисляет высоту дерева или поддерева.
        Высота:
            пустое дерево = -1
            узел без детей = 0

        Args:
            node: Корень поддерева (если None — берётся корень дерева).

        Returns:
            Целое число — высота.

        Сложность: O(n) — обход всех узлов.
        """
        if node is None:
            node = self.root
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))


    def is_valid_bst(self) -> bool:
        """
        Проверяет корректность структуры BST.

        Returns:
            True, если все узлы удовлетворяют свойству BST.

        Сложность: O(n)
        """

        def _validate(node, low, high):
            if node is None:
                return True
            if low is not None and node.value <= low:
                return False
            if high is not None and node.value >= high:
                return False
            return _validate(node.left, low, node.value) and \
                   _validate(node.right, node.value, high)

        return _validate(self.root, None, None)

    def to_list_inorder(self) -> List[Any]:
        """
        Возвращает элементы в порядке in-order (отсортированном).

        Returns:
            list значений.

        Сложность: O(n)
        """
        res = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                res.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return res



    def visualize_text(self) -> str:
        """
        Возвращает простую текстовую визуализацию дерева.
        Каждый уровень выводится с увеличенным отступом.

        Returns:
            Строка с визуальным представлением BST.
        """
        lines = []

        def _viz(node, depth):
            indent = " " * (depth * 4)
            if node is None:
                lines.append(indent + "·")
                return
            lines.append(indent + str(node.value))
            _viz(node.left, depth + 1)
            _viz(node.right, depth + 1)

        _viz(self.root, 0)
        return "\n".join(lines)
