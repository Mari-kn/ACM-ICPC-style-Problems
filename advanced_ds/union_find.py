# Union-Find (Disjoint Set Union)
# Efficiently track connected components with union and find operations.
# Path compression + union by rank gives near O(1) amortized per operation.
# Time Complexity: O(alpha(n)) amortized per operation | Space: O(n)
#
# Input format:
#   Line 1: n (elements 0..n-1), q (queries)
#   Next q lines: one of:
#     union u v
#     find u
#     connected u v
#     count          (number of components)
# Output: result of find/connected/count queries

import sys
input = sys.stdin.readline


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.components = n

    def find(self, x):
        """Path compression."""
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path splitting
            x = self.parent[x]
        return x

    def union(self, a, b):
        """Union by rank. Returns False if already connected."""
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        self.components -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def component_size(self, x):
        return self.size[self.find(x)]


class DSURollback:
    """DSU with rollback (no path compression, union by rank only).
    Supports undo of the last union operation. Useful for offline queries."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.history = []

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            self.history.append(None)
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.history.append((a, b, self.rank[a]))
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True

    def rollback(self):
        entry = self.history.pop()
        if entry is None:
            return
        a, b, old_rank = entry
        self.parent[b] = b
        self.rank[a] = old_rank


def main():
    n, q = map(int, input().split())
    dsu = DSU(n)
    for _ in range(q):
        parts = input().split()
        op = parts[0]
        if op == "union":
            u, v = int(parts[1]), int(parts[2])
            merged = dsu.union(u, v)
            print(f"union({u},{v}): {'merged' if merged else 'already connected'}")
        elif op == "find":
            u = int(parts[1])
            print(f"find({u}): {dsu.find(u)}")
        elif op == "connected":
            u, v = int(parts[1]), int(parts[2])
            print(f"connected({u},{v}): {dsu.connected(u, v)}")
        elif op == "count":
            print(f"components: {dsu.components}")


if __name__ == "__main__":
    main()
