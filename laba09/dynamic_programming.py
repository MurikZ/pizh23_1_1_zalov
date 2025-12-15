"""
Модуль dynamic_programming.py

Содержит классические алгоритмы динамического программирования:
- Числа Фибоначчи (наивный, нисходящий, восходящий подходы)
- Задача о рюкзаке (0-1 Knapsack) с восстановлением решения
- Наибольшая общая подпоследовательность (LCS)
- Расстояние Левенштейна
- Размен монет
- Наибольшая возрастающая подпоследовательность (LIS)

Все алгоритмы снабжены описанием и анализом сложности.
"""

from functools import lru_cache

# ЧИСЛА ФИБОНАЧЧИ

def fib_recursive(n: int) -> int:
    """
    Вычисляет n-е число Фибоначчи с помощью наивной рекурсии.

    :param n: номер числа Фибоначчи (n >= 0)
    :return: n-е число Фибоначчи

    Временная сложность: O(2^n)
    Пространственная сложность: O(n) — глубина стека рекурсии
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache(None)
def fib_memo(n: int) -> int:
    """
    Вычисляет n-е число Фибоначчи с использованием нисходящего
    подхода (мемоизация).

    :param n: номер числа Фибоначчи (n >= 0)
    :return: n-е число Фибоначчи

    Временная сложность: O(n)
    Пространственная сложность: O(n) — кэш + стек рекурсии
    """
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_iter(n: int) -> int:
    """
    Вычисляет n-е число Фибоначчи восходящим (итеративным) методом.

    :param n: номер числа Фибоначчи (n >= 0)
    :return: n-е число Фибоначчи

    Временная сложность: O(n)
    Пространственная сложность: O(1)
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# ЗАДАЧА О РЮКЗАКЕ (0-1 KNAPSACK)

def knapsack(weights: list, values: list, capacity: int) -> list:
    """
    Решает задачу о рюкзаке 0-1 методом динамического программирования.

    :param weights: список весов предметов
    :param values: список стоимостей предметов
    :param capacity: вместимость рюкзака
    :return: таблица dp, содержащая максимальные стоимости

    dp[i][w] — максимальная стоимость при использовании первых i предметов
    и вместимости рюкзака w.

    Временная сложность: O(nW)
    Пространственная сложность: O(nW)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp


def restore_knapsack(dp: list, weights: list, capacity: int) -> list:
    """
    Восстанавливает набор выбранных предметов для задачи о рюкзаке.

    :param dp: таблица динамического программирования
    :param weights: список весов предметов
    :param capacity: вместимость рюкзака
    :return: список индексов выбранных предметов
    """
    i = len(weights)
    w = capacity
    result = []

    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            result.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return result[::-1]

# НАИБОЛЬШАЯ ОБЩАЯ ПОДПОСЛЕДОВАТЕЛЬНОСТЬ (LCS)

def lcs(s1: str, s2: str) -> list:
    """
    Строит таблицу динамического программирования для LCS.

    :param s1: первая строка
    :param s2: вторая строка
    :return: таблица dp

    Временная сложность: O(nm)
    Пространственная сложность: O(nm)
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


def restore_lcs(dp: list, s1: str, s2: str) -> str:
    """
    Восстанавливает саму наибольшую общую подпоследовательность.

    :param dp: таблица динамического программирования
    :param s1: первая строка
    :param s2: вторая строка
    :return: строка — LCS
    """
    i, j = len(s1), len(s2)
    result = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))
# РАССТОЯНИЕ ЛЕВЕНШТЕЙНА (EDIT DISTANCE)

def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Вычисляет расстояние Левенштейна между двумя строками.

    Расстояние Левенштейна — это минимальное количество операций
    (вставка, удаление, замена), необходимых для превращения
    строки s1 в строку s2.

    :param s1: первая строка
    :param s2: вторая строка
    :return: расстояние Левенштейна

    dp[i][j] — минимальное число операций для преобразования
    первых i символов s1 в первые j символов s2.

    Временная сложность: O(nm)
    Пространственная сложность: O(nm)
    """
    n, m = len(s1), len(s2)

    # Инициализация таблицы
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Базовые случаи
    for i in range(n + 1):
        dp[i][0] = i   # удалить все символы s1
    for j in range(m + 1):
        dp[0][j] = j   # вставить все символы s2

    # Заполнение таблицы
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # удаление
                    dp[i][j - 1],     # вставка
                    dp[i - 1][j - 1]  # замена
                )

    return dp[n][m]
