# Fibonacci (DP vs Recursion)
# Compute the nth Fibonacci number using both approaches.
# Pure Recursion — Time: O(2^n), Space: O(n)        [exponential, impractical for large n]
# Bottom-up DP  — Time: O(n),   Space: O(1)         [optimal]
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: one integer n per line
# Output: "dp: x, recursive: x" per line
#
# Note: recursive approach is only feasible for small n (~35).
#       For large n, use DP only.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dp(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = fib_dp(n)
        # Only compute recursive for small n to avoid TLE
        if n <= 35:
            rec = fib_recursive(n)
            print(f"dp: {dp}, recursive: {rec}")
        else:
            print(f"dp: {dp}, recursive: skipped (n too large)")


if __name__ == "__main__":
    main()
