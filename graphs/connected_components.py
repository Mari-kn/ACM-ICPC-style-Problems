# Number of Connected Components
# Count connected components in an undirected graph.
# Three approaches: DFS, BFS, and Union-Find (Disjoint Set Union).
# Time Complexity: O(V + E) for DFS/BFS, O(V + E * alpha(V)) for DSU
# Space Complexity: O(V)
#
# Input format:
#   Line 1: V (vertices), E (edges)
#   Next E lines: u v (undirected edge, 0-indexed)
# Output: number of connected components, then vertices in each component

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def count_components_dfs(adj, V):
    visited = [False] * V
    components = []

    def dfs(u, comp):
        visited[u] = True
        comp.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v, comp)

    for u in range(V):
        if not visited[u]:
            comp = []
            dfs(u, comp)
            components.append(comp)
    return components


class DSU:
    """Disjoint Set Union with path compression and union by rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True


def count_components_dsu(edges, V):
    dsu = DSU(V)
    count = V
    for u, v in edges:
        if dsu.union(u, v):
            count -= 1
    return count


def main():
    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]
    edges = []
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    components = count_components_dfs(adj, V)
    dsu_count = count_components_dsu(edges, V)

    print(f"Components (DFS): {len(components)}")
    for i, comp in enumerate(components):
        print(f"  Component {i}: {' '.join(map(str, sorted(comp)))}")
    print(f"Components (DSU): {dsu_count}")


if __name__ == "__main__":
    main()
