# Lowest Common Ancestor (LCA)
# Find the lowest common ancestor of two nodes in a binary tree.
# Approach 1: Recursive DFS — O(n) time, O(h) space.
# Approach 2: Binary Lifting for repeated queries — O(n log n) preprocess, O(log n) per query.
# Time Complexity: O(n) per query naive | O(log n) per query with lifting
# Space Complexity: O(n)
#
# Input format:
#   Line 1: n (nodes, 0-indexed), q (queries)
#   Next n lines: left_child right_child (-1 means null), node 0 is root
#   Next q lines: u v (find LCA of u and v)
# Output: LCA for each query

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

LOG = 20


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(n, children):
    if n == 0:
        return None
    nodes = [TreeNode(i) for i in range(n)]
    for i in range(n):
        l, r = children[i]
        if l != -1:
            nodes[i].left = nodes[l]
        if r != -1:
            nodes[i].right = nodes[r]
    return nodes[0]


# ---- Approach 1: Recursive DFS (single query) ----

def lca_recursive(root, p, q):
    """Returns LCA of nodes with values p and q."""
    if not root or root.val == p or root.val == q:
        return root
    left = lca_recursive(root.left, p, q)
    right = lca_recursive(root.right, p, q)
    if left and right:
        return root
    return left if left else right


# ---- Approach 2: Binary Lifting (multiple queries) ----

def preprocess_lifting(n, children):
    """Build parent table, depths, and binary lifting table from adjacency."""
    # Build adjacency from children array
    adj = [[] for _ in range(n)]
    for i in range(n):
        l, r = children[i]
        if l != -1:
            adj[i].append(l)
            adj[l].append(i)
        if r != -1:
            adj[i].append(r)
            adj[r].append(i)

    depth = [0] * n
    up = [[-1] * n for _ in range(LOG)]

    # BFS from root (0) to set depths and parents
    visited = [False] * n
    queue = deque([0])
    visited[0] = True
    up[0][0] = 0  # root's parent is itself

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                up[0][v] = u
                queue.append(v)

    # Fill binary lifting table
    for k in range(1, LOG):
        for v in range(n):
            up[k][v] = up[k - 1][up[k - 1][v]]

    return depth, up


def lca_lifting(u, v, depth, up):
    # Bring to same depth
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for k in range(LOG):
        if (diff >> k) & 1:
            u = up[k][u]
    if u == v:
        return u
    for k in range(LOG - 1, -1, -1):
        if up[k][u] != up[k][v]:
            u = up[k][u]
            v = up[k][v]
    return up[0][u]


def main():
    n, q = map(int, input().split())
    children = []
    for _ in range(n):
        l, r = map(int, input().split())
        children.append((l, r))

    root = build_tree(n, children)
    depth, up = preprocess_lifting(n, children)

    for _ in range(q):
        u, v = map(int, input().split())
        # Recursive approach
        ans_rec = lca_recursive(root, u, v).val
        # Binary lifting approach
        ans_lift = lca_lifting(u, v, depth, up)
        print(f"LCA({u},{v}) = {ans_rec} (recursive), {ans_lift} (lifting)")


if __name__ == "__main__":
    main()
