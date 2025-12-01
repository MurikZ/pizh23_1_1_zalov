# hash_functions.py
"""
Реализованные хеш-функции для строк:
- simple_sum: простая сумма кодов символов (плохое распределение)
- poly_hash: полиномиальная (rolling) хеш-функция (хорошее распределение)
- djb2: функция DJB2 (быстрая и неплохо распределяет для текстов)
"""
from typing import Callable

def simple_sum(s: str) -> int:
    """Простая сумма кодов символов.
    Быстрая, но даёт много коллизий при перестановках символов."""
    return sum(ord(c) for c in s)


def poly_hash(s: str, base: int = 257, mod: int = 2**61 - 1) -> int:
    """Полиномиальная (rolling) хеш-функция.
    Хорошее распределение при выбранном base и большом mod.
    Возвращает значение в [0, mod-1]."""
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod
    return h


def djb2(s: str) -> int:
    """DJB2 — h = 5381; for c: h = h*33 + ord(c)
    Возвращает 64-битное значение (симуляция unsigned 64-bit)."""
    h = 5381
    for c in s:
        h = ((h << 5) + h) + ord(c)
    return h & 0xFFFFFFFFFFFFFFFF


# optional helper: list of functions
HASH_FUNCTIONS = {
    "simple_sum": simple_sum,
    "poly_hash": poly_hash,
    "djb2": djb2
}
