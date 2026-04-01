# Fenwick Tree (Binary Indexed Tree)
# Supports prefix sum queries and point updates in O(log n).
# Simpler and faster constant than segment tree for sum/update operations.
# Time Complexity: O(log n) per operation | Space: O(n)
#
# Input format:
#   Line 1: n (array size), q (queries)
#   Line 2: n space-separated integers (initial array)
#   Next q lines: one of:
#     update i delta    (add delta to arr[i], 0-indexed)
#     query l r         (sum of arr[l..r], 0-indexed inclusive)
#     prefix r          (sum of arr[0..r])
# Output: result of query/prefix operations

import sys
input = sys.stdin.readline


class FenwickTree:
    """1-indexed internally, 0-indexed API."""
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @classmethod
    def from_array(cls, arr):
        """Build in O(n)."""
        n = len(arr)
        ft = cls(n)
        for i in range(n):
            ft.tree[i + 1] = arr[i]
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j <= n:
                ft.tree[j] += ft.tree[i]
        return ft

    def update(self, i, delta):
        """Add delta to arr[i] (0-indexed)."""
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        """Sum of arr[0..i] (0-indexed, inclusive)."""
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        """Sum of arr[l..r] (0-indexed, inclusive)."""
        if l == 0:
            return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)


class FenwickTree2D:
    """2D Fenwick Tree for point update and rectangle sum queries.
    Time: O(log(n) * log(m)) per operation."""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]

    def update(self, r, c, delta):
        """Add delta to cell (r, c), 0-indexed."""
        r += 1
        while r <= self.rows:
            j = c + 1
            while j <= self.cols:
                self.tree[r][j] += delta
                j += j & -j
            r += r & -r

    def prefix_sum(self, r, c):
        """Sum of rectangle (0,0) to (r,c), 0-indexed inclusive."""
        s = 0
        r += 1
        while r > 0:
            j = c + 1
            while j > 0:
                s += self.tree[r][j]
                j -= j & -j
            r -= r & -r
        return s

    def range_sum(self, r1, c1, r2, c2):
        """Sum of rectangle (r1,c1) to (r2,c2), 0-indexed inclusive."""
        s = self.prefix_sum(r2, c2)
        if r1 > 0:
            s -= self.prefix_sum(r1 - 1, c2)
        if c1 > 0:
            s -= self.prefix_sum(r2, c1 - 1)
        if r1 > 0 and c1 > 0:
            s += self.prefix_sum(r1 - 1, c1 - 1)
        return s


def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    ft = FenwickTree.from_array(arr)

    for _ in range(q):
        parts = input().split()
        op = parts[0]
        if op == "update":
            i, delta = int(parts[1]), int(parts[2])
            ft.update(i, delta)
        elif op == "query":
            l, r = int(parts[1]), int(parts[2])
            print(ft.range_sum(l, r))
        elif op == "prefix":
            r = int(parts[1])
            print(ft.prefix_sum(r))


if __name__ == "__main__":
    main()
