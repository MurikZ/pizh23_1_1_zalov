"""
task_solutions.py
Практические задачи:
1. Проверка сбалансированности скобок с использованием стека (list)
2. Симуляция очереди печати (deque)
3. Проверка палиндрома с использованием дека (deque)
"""

from collections import deque
from typing import Iterable


def is_brackets_balanced(s: str) -> bool:
    """Проверка сбалансированности скобок. O(n)"""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def simulate_print_queue(jobs: Iterable[str]):
    """Симуляция очереди печати. FIFO (deque)."""
    dq = deque(jobs)
    processed = []
    while dq:
        job = dq.popleft()
        processed.append(f"printed:{job}")
    return processed


def is_palindrome(seq: Iterable) -> bool:
    """Проверка палиндрома с использованием deque. O(n)"""
    dq = deque(seq)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


if __name__ == "__main__":
    # Тесты
    assert is_brackets_balanced("{[()()]}") is True
    assert is_brackets_balanced("{[(])}") is False
    assert simulate_print_queue(["a", "b", "c"]) == ["printed:a", "printed:b", "printed:c"]
    assert is_palindrome("radar") is True
    assert is_palindrome([1, 2, 3, 2, 1]) is True
    assert is_palindrome([1, 2, 3]) is False
    print("Все тесты успешно пройдены.")
