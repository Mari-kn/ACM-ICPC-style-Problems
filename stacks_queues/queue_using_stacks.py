# Implement Queue using Stacks
# Implement a FIFO queue using only two stacks.
# Amortized O(1) per operation using lazy transfer from input to output stack.
# Time Complexity: O(1) amortized per operation | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of operations q
#   Next q lines: one of:
#     push x
#     pop
#     peek
#     empty
# Output: result of pop, peek, and empty operations, one per line

import sys
input = sys.stdin.readline


class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []   # for push
        self.out_stack = []  # for pop/peek

    def push(self, x):
        self.in_stack.append(x)

    def _transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self):
        self._transfer()
        return self.out_stack.pop()

    def peek(self):
        self._transfer()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


def main():
    q = int(input())
    queue = QueueUsingStacks()
    for _ in range(q):
        parts = input().split()
        op = parts[0]
        if op == "push":
            queue.push(int(parts[1]))
        elif op == "pop":
            print(queue.pop())
        elif op == "peek":
            print(queue.peek())
        elif op == "empty":
            print(queue.empty())


if __name__ == "__main__":
    main()
