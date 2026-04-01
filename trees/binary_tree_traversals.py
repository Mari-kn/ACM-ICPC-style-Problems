# Binary Tree Traversals (Inorder, Preorder, Postorder)
# Recursive and iterative (stack-based) implementations for all three.
# Also includes level-order (BFS) traversal.
# Time Complexity: O(n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: n (number of nodes, 0-indexed)
#   Next n lines: left_child right_child (-1 means null)
#   Node 0 is the root.
# Output: all four traversal orders

import sys
from collections import deque
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


# ---- Recursive ----

def inorder_rec(root):
    if not root:
        return []
    return inorder_rec(root.left) + [root.val] + inorder_rec(root.right)


def preorder_rec(root):
    if not root:
        return []
    return [root.val] + preorder_rec(root.left) + preorder_rec(root.right)


def postorder_rec(root):
    if not root:
        return []
    return postorder_rec(root.left) + postorder_rec(root.right) + [root.val]


# ---- Iterative ----

def inorder_iter(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result


def preorder_iter(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def postorder_iter(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def main():
    n = int(input())
    children = []
    for _ in range(n):
        l, r = map(int, input().split())
        children.append((l, r))
    root = build_tree(n, children)

    print("inorder:    ", *inorder_iter(root))
    print("preorder:   ", *preorder_iter(root))
    print("postorder:  ", *postorder_iter(root))
    levels = level_order(root)
    print("level-order:", " | ".join(" ".join(map(str, lv)) for lv in levels))


if __name__ == "__main__":
    main()
