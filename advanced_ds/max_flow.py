# Max Flow (Ford-Fulkerson with Edmonds-Karp BFS)
# Find the maximum flow from source to sink in a flow network.
# Edmonds-Karp uses BFS to find augmenting paths (shortest path heuristic).
# Also includes Dinic's algorithm for better performance on dense graphs.
# Time Complexity: O(VE^2) Edmonds-Karp, O(V^2 * E) Dinic's | Space: O(V + E)
#
# Input format:
#   Line 1: V (vertices), E (edges), S (source), T (sink)
#   Next E lines: u v capacity (directed edge)
# Output: maximum flow value and the flow on each edge

import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')


class EdmondsKarp:
    """Max flow using BFS augmenting paths."""
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]  # adjacency list of edge indices
        self.edges = []  # (to, capacity, flow)

    def add_edge(self, u, v, cap):
        self.graph[u].append(len(self.edges))
        self.edges.append([v, cap, 0])
        self.graph[v].append(len(self.edges))
        self.edges.append([u, 0, 0])  # reverse edge

    def bfs(self, s, t, parent):
        visited = [False] * self.n
        visited[s] = True
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for eid in self.graph[u]:
                v, cap, flow = self.edges[eid]
                if not visited[v] and cap - flow > 0:
                    visited[v] = True
                    parent[v] = eid
                    if v == t:
                        return True
                    queue.append(v)
        return False

    def max_flow(self, s, t):
        total = 0
        parent = [-1] * self.n
        while self.bfs(s, t, parent):
            # Find bottleneck
            path_flow = INF
            v = t
            while v != s:
                eid = parent[v]
                path_flow = min(path_flow, self.edges[eid][1] - self.edges[eid][2])
                v = self.edges[eid ^ 1][0]  # reverse edge leads back
            # Update flow
            v = t
            while v != s:
                eid = parent[v]
                self.edges[eid][2] += path_flow
                self.edges[eid ^ 1][2] -= path_flow
                v = self.edges[eid ^ 1][0]
            total += path_flow
            parent = [-1] * self.n
        return total


class Dinic:
    """Dinic's algorithm — faster for dense graphs."""
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.edges = []

    def add_edge(self, u, v, cap):
        self.graph[u].append(len(self.edges))
        self.edges.append([v, cap, 0])
        self.graph[v].append(len(self.edges))
        self.edges.append([u, 0, 0])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for eid in self.graph[u]:
                v, cap, flow = self.edges[eid]
                if self.level[v] == -1 and cap - flow > 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1

    def dfs(self, u, t, pushed):
        if u == t:
            return pushed
        while self.iter[u] < len(self.graph[u]):
            eid = self.graph[u][self.iter[u]]
            v, cap, flow = self.edges[eid]
            if self.level[v] == self.level[u] + 1 and cap - flow > 0:
                d = self.dfs(v, t, min(pushed, cap - flow))
                if d > 0:
                    self.edges[eid][2] += d
                    self.edges[eid ^ 1][2] -= d
                    return d
            self.iter[u] += 1
        return 0

    def max_flow(self, s, t):
        total = 0
        while self.bfs(s, t):
            self.iter = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                total += f
        return total


def main():
    V, E, S, T = map(int, input().split())
    ek = EdmondsKarp(V)
    dinic = Dinic(V)

    for _ in range(E):
        u, v, cap = map(int, input().split())
        ek.add_edge(u, v, cap)
        dinic.add_edge(u, v, cap)

    flow_ek = ek.max_flow(S, T)
    flow_dinic = dinic.max_flow(S, T)

    print(f"Edmonds-Karp max flow: {flow_ek}")
    print(f"Dinic max flow: {flow_dinic}")

    # Print edge flows from Edmonds-Karp (forward edges only)
    print("Edge flows:")
    for i in range(0, len(ek.edges), 2):
        v, cap, flow = ek.edges[i]
        u = ek.edges[i + 1][0]
        if flow > 0:
            print(f"  {u} -> {v}: {flow}/{cap}")


if __name__ == "__main__":
    main()
