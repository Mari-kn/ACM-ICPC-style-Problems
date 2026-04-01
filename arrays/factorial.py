# Factorial (Iterative & Recursive)
# Compute n! using both approaches.
# Iterative — Time: O(n), Space: O(1)
# Recursive — Time: O(n), Space: O(n) due to call stack
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: one integer n per line
# Output: "iterative: x, recursive: x" per line

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        it = factorial_iterative(n)
        rec = factorial_recursive(n)
        print(f"iterative: {it}, recursive: {rec}")


if __name__ == "__main__":
    main()
