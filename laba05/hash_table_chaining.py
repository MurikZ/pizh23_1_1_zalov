# hash_table_chaining.py
"""
Хеш-таблица методом цепочек с динамическим масштабированием.
- resize_enabled: если True, выполняем rehash при α > 0.75 (увеличение в 2 раза)
  и уменьшаем при α < 0.2 (минимум capacity = 8).
- collision_count: число вставок, когда бакет был непуст (индикатор коллизий).
"""
from typing import Callable, List, Tuple

class HashTableChaining:
    def __init__(self, capacity: int = 8, hash_func: Callable[[str], int] = None, resize_enabled: bool = True):
        self.capacity = max(8, capacity)
        self.hash_func = hash_func or (lambda s: sum(ord(c) for c in s))
        self.buckets: List[List[Tuple[str, object]]] = [[] for _ in range(self.capacity)]
        self.size = 0
        self.resize_enabled = resize_enabled
        self.collision_count = 0

    def _index(self, key: str) -> int:
        return self.hash_func(key) % self.capacity

    def _rehash(self, new_capacity: int):
        old_items = [(k, v) for bucket in self.buckets for (k, v) in bucket]
        self.capacity = max(8, int(new_capacity))
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        self.collision_count = 0
        for k, v in old_items:
            self.insert(k, v)

    def insert(self, key: str, value):
        idx = self._index(key)
        bucket = self.buckets[idx]

        # update existing
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # new key
        if bucket:
            self.collision_count += 1
        bucket.append((key, value))
        self.size += 1

        if self.resize_enabled and (self.size / self.capacity) > 0.75:
            self._rehash(self.capacity * 2)

    def find(self, key: str):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def delete(self, key: str):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                if self.resize_enabled and self.capacity > 8 and (self.size / self.capacity) < 0.2:
                    self._rehash(max(8, self.capacity // 2))
                return
        raise KeyError(key)
