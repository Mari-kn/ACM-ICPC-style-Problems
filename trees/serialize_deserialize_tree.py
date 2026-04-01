# Serialize & Deserialize Binary Tree
# Convert a binary tree to a string and reconstruct it back.
# Approach 1: Preorder with null markers — O(n) time and space.
# Approach 2: Level-order (BFS) with null markers — O(n) time and space.
#
# Input format:
#   Line 1: n (nodes, 0-indexed)
#   Next n lines: left_child right_child (-1 means null), node 0 is root
# Output: serialized string, then traversal of deserialized tree to verify

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

NULL = "#"
SEP = ","


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


# ---- Preorder Serialization ----

def serialize_preorder(root):
    tokens = []

    def dfs(node):
        if not node:
            tokens.append(NULL)
            return
        tokens.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return SEP.join(tokens)


def deserialize_preorder(data):
    tokens = iter(data.split(SEP))

    def build():
        val = next(tokens)
        if val == NULL:
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()


# ---- Level-order (BFS) Serialization ----

def serialize_bfs(root):
    if not root:
        return NULL
    tokens = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            tokens.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            tokens.append(NULL)
    # Strip trailing nulls
    while tokens and tokens[-1] == NULL:
        tokens.pop()
    return SEP.join(tokens)


def deserialize_bfs(data):
    if data == NULL:
        return None
    tokens = data.split(SEP)
    root = TreeNode(int(tokens[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(tokens):
        node = queue.popleft()
        if i < len(tokens) and tokens[i] != NULL:
            node.left = TreeNode(int(tokens[i]))
            queue.append(node.left)
        i += 1
        if i < len(tokens) and tokens[i] != NULL:
            node.right = TreeNode(int(tokens[i]))
            queue.append(node.right)
        i += 1
    return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def main():
    n = int(input())
    children = []
    for _ in range(n):
        l, r = map(int, input().split())
        children.append((l, r))
    root = build_tree(n, children)

    # Preorder serialization
    s1 = serialize_preorder(root)
    r1 = deserialize_preorder(s1)
    print(f"preorder serialized: {s1}")
    print(f"preorder verified:   {' '.join(map(str, inorder(r1)))}")

    # BFS serialization
    s2 = serialize_bfs(root)
    r2 = deserialize_bfs(s2)
    print(f"bfs serialized:      {s2}")
    print(f"bfs verified:        {' '.join(map(str, inorder(r2)))}")


if __name__ == "__main__":
    main()
