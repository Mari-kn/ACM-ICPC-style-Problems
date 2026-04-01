# Bellman-Ford Algorithm — Single Source Shortest Path
# Handles negative edge weights and detects negative cycles.
# Time Complexity: O(V * E) | Space Complexity: O(V)
#
# Input format:
#   Line 1: V (vertices), E (edges), S (source, 0-indexed)
#   Next E lines: u v w (directed edge with weight w, can be negative)
# Output: shortest distances from S, or "NEGATIVE CYCLE" if one exists

import sys
input = sys.stdin.readline

INF = float('inf')


def bellman_ford(V, edges, source):
    dist = [INF] * V
    parent = [-1] * V
    dist[source] = 0

    # Relax all edges V-1 times
    for _ in range(V - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break

    # Check for negative cycles (Vth relaxation)
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None, None  # negative cycle detected

    return dist, parent


def main():
    V, E, S = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    dist, parent = bellman_ford(V, edges, S)

    if dist is None:
        print("NEGATIVE CYCLE")
    else:
        for v in range(V):
            d = dist[v] if dist[v] != INF else -1
            print(f"to {v}: {d}")


if __name__ == "__main__":
    main()
