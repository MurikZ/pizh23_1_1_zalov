"""
recursion_tasks.py
Практические задачи:
- бинарный поиск (рекурсивный)
- рекурсивный обход файловой системы
- решение задачи «Ханойские башни»
"""

import os
from typing import List, Tuple


def binary_search_recursive(arr, target, left, right):
    """
    Рекурсивный бинарный поиск.
    Возвращает индекс элемента target или -1, если не найден.
    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def walk_fs_recursive(path: str, indent: int = 0) -> None:
    """
    Рекурсивный обход файловой системы.
    Печатает дерево каталогов и файлов, начиная с path.
    Глубина рекурсии = глубина вложенности каталогов.
    """
    try:
        entries = sorted(os.listdir(path))
    except (PermissionError, FileNotFoundError):
        print("  " * indent + f"[Ошибка доступа] {path}")
        return

    for name in entries:
        full = os.path.join(path, name)
        print("  " * indent + name)
        if os.path.isdir(full):
            walk_fs_recursive(full, indent + 1)


def hanoi(n: int, source: str, target: str, aux: str) -> List[Tuple[int, str, str]]:
    """
    Решение задачи Ханойских башен.
    Возвращает список перемещений (номер диска, откуда, куда).
    Временная сложность: O(2^n)
    Глубина рекурсии: n
    """
    moves = []
    if n == 0:
        return moves
    if n == 1:
        moves.append((1, source, target))
        return moves

    moves += hanoi(n - 1, source, aux, target)
    moves.append((n, source, target))
    moves += hanoi(n - 1, aux, target, source)
    return moves
