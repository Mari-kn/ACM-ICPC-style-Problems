# DFS (Depth First Search)
# Traverse or search a graph by exploring as far as possible along each branch.
# Both recursive and iterative (stack-based) implementations.
# Time Complexity: O(V + E) | Space Complexity: O(V)
#
# Input format:
#   Line 1: V (vertices), E (edges), S (start vertex, 0-indexed)
#   Next E lines: u v (undirected edge)
# Output: DFS traversal order

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs_recursive(adj, start, V):
    visited = [False] * V
    order = []

    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(start)
    return order


def dfs_iterative(adj, start, V):
    visited = [False] * V
    stack = [start]
    order = []
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        # Push neighbors in reverse for consistent left-to-right order
        for v in reversed(adj[u]):
            if not visited[v]:
                stack.append(v)
    return order


def main():
    V, E, S = map(int, input().split())
    adj = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    # Sort adjacency lists for deterministic order
    for i in range(V):
        adj[i].sort()
    rec = dfs_recursive(adj, S, V)
    it = dfs_iterative(adj, S, V)
    print("recursive:", *rec)
    print("iterative:", *it)


if __name__ == "__main__":
    main()
