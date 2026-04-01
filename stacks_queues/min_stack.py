# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in O(1).
# Uses an auxiliary stack to track minimums at each level.
# Time Complexity: O(1) all operations | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of operations q
#   Next q lines: one of:
#     push x
#     pop
#     top
#     getMin
# Output: result of top and getMin operations, one per line

import sys
input = sys.stdin.readline


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


def main():
    q = int(input())
    ms = MinStack()
    for _ in range(q):
        parts = input().split()
        op = parts[0]
        if op == "push":
            ms.push(int(parts[1]))
        elif op == "pop":
            ms.pop()
        elif op == "top":
            print(ms.top())
        elif op == "getMin":
            print(ms.get_min())


if __name__ == "__main__":
    main()
