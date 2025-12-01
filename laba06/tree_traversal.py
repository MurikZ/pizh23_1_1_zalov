"""
tree_traversal.py

Рекурсивные и итеративные обходы бинарного дерева поиска.
Обходы:
    - in-order (симметричный)
    - pre-order (прямой)
    - post-order (обратный)
    - итеративный in-order с использованием стека
"""

from __future__ import annotations
from typing import Optional, Callable, Any, List
from binary_search_tree import TreeNode


def inorder_recursive(node: Optional[TreeNode], visit: Callable[[Any], None]) -> None:
    """
    Рекурсивный симметричный обход дерева (left, root, right).

    Args:
        node: Текущий узел.
        visit: Функция, выполняемая над каждым значением (например, print).

    Сложность: O(n)
    """
    if node is None:
        return
    inorder_recursive(node.left, visit)
    visit(node.value)
    inorder_recursive(node.right, visit)


def preorder_recursive(node: Optional[TreeNode], visit: Callable[[Any], None]) -> None:
    """
    Рекурсивный прямой обход (root, left, right).

    Args:
        node: Узел.
        visit: Обработчик значения.

    Сложность: O(n)
    """
    if node is None:
        return
    visit(node.value)
    preorder_recursive(node.left, visit)
    preorder_recursive(node.right, visit)


def postorder_recursive(node: Optional[TreeNode], visit: Callable[[Any], None]) -> None:
    """
    Рекурсивный обратный обход (left, right, root).

    Args:
        node: Узел.
        visit: Функция обработки значения.

    Сложность: O(n)
    """
    if node is None:
        return
    postorder_recursive(node.left, visit)
    postorder_recursive(node.right, visit)
    visit(node.value)


def inorder_iterative(node: Optional[TreeNode], visit: Callable[[Any], None]) -> None:
    """
    Итеративный симметричный обход с использованием стека.

    Алгоритм:
        - Идём влево, кладём узлы в стек.
        - Извлекаем вершину стека, посещаем её.
        - Переходим в правое поддерево.

    Args:
        node: Корень дерева.
        visit: Обработчик значения.

    Сложность:
        Время: O(n)
        Память: O(h), где h — высота дерева.
    """
    stack: List[TreeNode] = []
    current = node
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        visit(current.value)
        current = current.right
