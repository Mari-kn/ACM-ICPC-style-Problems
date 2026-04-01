# Dijkstra's Algorithm — Shortest Path from Single Source
# Works on graphs with non-negative edge weights.
# Uses a min-heap (priority queue) for efficient extraction.
# Time Complexity: O((V + E) log V) | Space Complexity: O(V + E)
#
# Input format:
#   Line 1: V (vertices), E (edges), S (source, 0-indexed)
#   Next E lines: u v w (directed edge with weight w)
# Output: shortest distances from S to all vertices, then shortest path to each vertex

import sys
import heapq
input = sys.stdin.readline

INF = float('inf')


def dijkstra(adj, source, V):
    dist = [INF] * V
    parent = [-1] * V
    dist[source] = 0
    pq = [(0, source)]  # (distance, vertex)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent


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
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
    dist, parent = dijkstra(adj, S, V)
    for v in range(V):
        d = dist[v] if dist[v] != INF else -1
        path = reconstruct_path(parent, v) if dist[v] != INF else []
        print(f"to {v}: dist={d}, path={' -> '.join(map(str, path))}")


if __name__ == "__main__":
    main()
