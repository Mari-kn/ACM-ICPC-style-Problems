# Detect Cycle in Graph
# Directed graph: DFS coloring (white/gray/black).
# Undirected graph: DFS with parent tracking or Union-Find.
# Time Complexity: O(V + E) | Space Complexity: O(V)
#
# Input format:
#   Line 1: V (vertices), E (edges), type ("directed" or "undirected")
#   Next E lines: u v (edge, 0-indexed)
# Output: "CYCLE FOUND" or "NO CYCLE"

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def has_cycle_directed(adj, V):
    """DFS coloring: GRAY back-edge means cycle."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * V

    def dfs(u):
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False

    for u in range(V):
        if color[u] == WHITE:
            if dfs(u):
                return True
    return False


def has_cycle_undirected_dfs(adj, V):
    """DFS with parent tracking."""
    visited = [False] * V

    def dfs(u, parent):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for u in range(V):
        if not visited[u]:
            if dfs(u, -1):
                return True
    return False


class DSU:
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


def has_cycle_undirected_dsu(edges, V):
    """Union-Find: if two endpoints already in same set, cycle exists."""
    dsu = DSU(V)
    for u, v in edges:
        if not dsu.union(u, v):
            return True
    return False


def main():
    parts = input().split()
    V, E = int(parts[0]), int(parts[1])
    graph_type = parts[2]

    adj = [[] for _ in range(V)]
    edges = []
    for _ in range(E):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append(v)
        if graph_type == "undirected":
            adj[v].append(u)

    if graph_type == "directed":
        result = has_cycle_directed(adj, V)
    else:
        result = has_cycle_undirected_dfs(adj, V)
        result_dsu = has_cycle_undirected_dsu(edges, V)
        # Both should agree
        assert result == result_dsu

    print("CYCLE FOUND" if result else "NO CYCLE")


if __name__ == "__main__":
    main()
