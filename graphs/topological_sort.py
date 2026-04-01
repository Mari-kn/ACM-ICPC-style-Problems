# Topological Sort
# Linear ordering of vertices in a DAG such that for every edge u->v, u comes before v.
# Two approaches: Kahn's algorithm (BFS + in-degree) and DFS-based.
# Time Complexity: O(V + E) | Space Complexity: O(V)
#
# Input format:
#   Line 1: V (vertices), E (edges)
#   Next E lines: u v (directed edge u -> v, 0-indexed)
# Output: topological order, or "NOT A DAG" if cycle exists

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def topo_sort_kahn(adj, V):
    """Kahn's algorithm — BFS with in-degree tracking."""
    in_deg = [0] * V
    for u in range(V):
        for v in adj[u]:
            in_deg[v] += 1

    queue = deque(v for v in range(V) if in_deg[v] == 0)
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)

    if len(order) != V:
        return None  # cycle exists
    return order


def topo_sort_dfs(adj, V):
    """DFS-based — post-order reversal."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * V
    order = []
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == GRAY:
                has_cycle = True
                return
            if color[v] == WHITE:
                dfs(v)
                if has_cycle:
                    return
        color[u] = BLACK
        order.append(u)

    for u in range(V):
        if color[u] == WHITE:
            dfs(u)
            if has_cycle:
                return None

    return order[::-1]


def main():
    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)

    kahn = topo_sort_kahn(adj, V)
    dfs_order = topo_sort_dfs(adj, V)

    if kahn is None:
        print("NOT A DAG")
    else:
        print("Kahn:", *kahn)
        print("DFS: ", *dfs_order)


if __name__ == "__main__":
    main()
