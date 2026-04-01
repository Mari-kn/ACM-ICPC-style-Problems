# Balanced Binary Tree
# A binary tree is balanced if for every node, the height difference
# between left and right subtrees is at most 1.
# Single DFS pass: return -1 early if any subtree is unbalanced.
# Time Complexity: O(n) | Space Complexity: O(h)
#
# Input format:
#   Line 1: n (nodes, 0-indexed)
#   Next n lines: left_child right_child (-1 means null), node 0 is root
# Output: "Balanced" or "Not Balanced"

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


def is_balanced(root):
    def check(node):
        """Returns height if balanced, -1 if not."""
        if not node:
            return 0
        lh = check(node.left)
        if lh == -1:
            return -1
        rh = check(node.right)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh) + 1

    return check(root) != -1


def main():
    n = int(input())
    children = []
    for _ in range(n):
        l, r = map(int, input().split())
        children.append((l, r))
    root = build_tree(n, children)
    print("Balanced" if is_balanced(root) else "Not Balanced")


if __name__ == "__main__":
    main()
