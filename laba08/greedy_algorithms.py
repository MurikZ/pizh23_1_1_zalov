from heapq import heappush, heappop

def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])
    result = []
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:
            result.append((start, end))
            last_end = end

    return result


def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0.0

    for value, weight in items:
        if capacity <= 0:
            break

        take = min(weight, capacity)
        total_value += take * (value / weight)
        capacity -= take

    return total_value


class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(frequencies):
    heap = []

    for char, freq in frequencies.items():
        heappush(heap, HuffmanNode(freq, char))

    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        merged = HuffmanNode(a.freq + b.freq, None, a, b)
        heappush(heap, merged)

    return heap[0]


def build_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}

    if node.char is not None:
        codes[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codes)
        build_codes(node.right, prefix + "1", codes)

    return codes


def greedy_coin_change(coins, amount):
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result


def kruskal(vertices, edges):
    parent = {v: v for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    mst = []

    edges.sort()
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst
