# BFS (Breadth First Search)
# Traverse a graph level by level. Also computes shortest distances in unweighted graphs.
# Time Complexity: O(V + E) | Space Complexity: O(V)
#
# Input format:
#   Line 1: V (vertices), E (edges), S (start vertex, 0-indexed)
#   Next E lines: u v (undirected edge)
# Output: BFS traversal order, then shortest distances from S

import sys
from collections import deque
input = sys.stdin.readline


def bfs(adj, start, V):
    visited = [False] * V
    dist = [-1] * V
    parent = [-1] * V
    order = []
    queue = deque([start])
    visited[start] = True
    dist[start] = 0

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    return order, dist, parent


def reconstruct_path(parent, target):
    path = []
    while target != -1:
        path.append(target)
        target = parent[target]
    return path[::-1]


def main():
    V, E, S = map(int, input().split())
    adj = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(V):
        adj[i].sort()
    order, dist, parent = bfs(adj, S, V)
    print("order:", *order)
    print("dist:", *dist)


if __name__ == "__main__":
    main()
