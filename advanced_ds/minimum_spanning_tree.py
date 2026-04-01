# Minimum Spanning Tree (Kruskal / Prim)
# Kruskal: sort edges by weight, greedily add using Union-Find. O(E log E).
# Prim: grow MST from a source using min-heap. O((V + E) log V).
#
# Input format:
#   Line 1: V (vertices), E (edges)
#   Next E lines: u v w (undirected edge with weight w, 0-indexed)
# Output: MST total weight and edges

import sys
import heapq
input = sys.stdin.readline


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


def kruskal(V, edges):
    """Sort edges by weight, greedily add with DSU.
    Time: O(E log E) | Space: O(V)"""
    edges_sorted = sorted(edges, key=lambda e: e[2])
    dsu = DSU(V)
    mst_weight = 0
    mst_edges = []

    for u, v, w in edges_sorted:
        if dsu.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))
            if len(mst_edges) == V - 1:
                break

    return mst_weight, mst_edges


def prim(V, adj, start=0):
    """Grow MST from start using min-heap.
    Time: O((V + E) log V) | Space: O(V + E)"""
    visited = [False] * V
    mst_weight = 0
    mst_edges = []
    # (weight, vertex, parent)
    pq = [(0, start, -1)]

    while pq and len(mst_edges) < V - 1:
        w, u, parent = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += w
        if parent != -1:
            mst_edges.append((parent, u, w))
        for v, wt in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (wt, v, u))

    return mst_weight, mst_edges


def main():
    V, E = map(int, input().split())
    edges = []
    adj = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))

    kw, ke = kruskal(V, edges)
    pw, pe = prim(V, adj)

    print(f"Kruskal MST weight: {kw}")
    for u, v, w in ke:
        print(f"  {u} -- {v} (w={w})")
    print(f"Prim MST weight: {pw}")
    for u, v, w in pe:
        print(f"  {u} -- {v} (w={w})")


if __name__ == "__main__":
    main()
