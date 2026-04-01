# Floyd-Warshall Algorithm — All Pairs Shortest Path
# Computes shortest paths between every pair of vertices.
# Can detect negative cycles (diagonal becomes negative).
# Time Complexity: O(V^3) | Space Complexity: O(V^2)
#
# Input format:
#   Line 1: V (vertices), E (edges)
#   Next E lines: u v w (directed edge with weight w)
# Output: V x V distance matrix (INF shown as "INF")

import sys
input = sys.stdin.readline

INF = float('inf')


def floyd_warshall(V, edges):
    dist = [[INF] * V for _ in range(V)]
    nxt = [[-1] * V for _ in range(V)]

    for i in range(V):
        dist[i][i] = 0
        nxt[i][i] = i

    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            nxt[u][v] = v

    for k in range(V):
        for i in range(V):
            if dist[i][k] == INF:
                continue
            for j in range(V):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]

    # Check for negative cycles
    has_neg_cycle = any(dist[i][i] < 0 for i in range(V))

    return dist, nxt, has_neg_cycle


def reconstruct_path(nxt, u, v):
    if nxt[u][v] == -1:
        return []
    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path


def main():
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    dist, nxt, has_neg_cycle = floyd_warshall(V, edges)

    if has_neg_cycle:
        print("NEGATIVE CYCLE DETECTED")
    for i in range(V):
        row = []
        for j in range(V):
            row.append("INF" if dist[i][j] == INF else str(dist[i][j]))
        print(" ".join(row))


if __name__ == "__main__":
    main()
