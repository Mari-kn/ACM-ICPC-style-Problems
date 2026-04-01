# Evaluate Reverse Polish Notation
# Evaluate an expression in Reverse Polish Notation (postfix).
# Supported operators: +, -, *, /  (integer division truncates toward zero).
# Time Complexity: O(n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: space-separated tokens
# Output: result per line

import sys
input = sys.stdin.readline


def eval_rpn(tokens):
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),  # truncate toward zero
    }
    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    return stack[0]


def main():
    t = int(input())
    for _ in range(t):
        tokens = input().split()
        print(eval_rpn(tokens))


if __name__ == "__main__":
    main()
