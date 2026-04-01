# Diameter of Binary Tree
# The diameter is the longest path between any two nodes (measured in edges).
# The path may or may not pass through the root.
# Single DFS pass tracking height and updating global max.
# Time Complexity: O(n) | Space Complexity: O(h) where h = height
#
# Input format:
#   Line 1: n (nodes, 0-indexed)
#   Next n lines: left_child right_child (-1 means null), node 0 is root
# Output: diameter (number of edges)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


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


def diameter(root):
    max_diam = 0

    def height(node):
        nonlocal max_diam
        if not node:
            return -1  # -1 so leaf height = 0
        lh = height(node.left)
        rh = height(node.right)
        # Diameter through this node = left height + right height + 2
        max_diam = max(max_diam, lh + rh + 2)
        return max(lh, rh) + 1

    height(root)
    return max_diam


def diameter_iterative(root):
    """Iterative post-order to avoid stack overflow on deep trees."""
    if not root:
        return 0
    max_diam = 0
    height_map = {None: -1}
    stack = [(root, False)]

    while stack:
        node, processed = stack.pop()
        if processed:
            lh = height_map.get(node.left, -1)
            rh = height_map.get(node.right, -1)
            max_diam = max(max_diam, lh + rh + 2)
            height_map[node] = max(lh, rh) + 1
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return max_diam


def main():
    n = int(input())
    children = []
    for _ in range(n):
        l, r = map(int, input().split())
        children.append((l, r))
    root = build_tree(n, children)
    print(diameter(root))


if __name__ == "__main__":
    main()
