# Climbing Stairs
# You can climb 1 or 2 steps at a time. Count the number of distinct ways to reach step n.
# Equivalent to Fibonacci. Bottom-up DP.
# Time Complexity: O(n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: integer n
# Output: number of ways per line

import sys
input = sys.stdin.readline


def climbing_stairs(n):
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


def climbing_stairs_k_steps(n, k):
    """Generalized: can climb 1 to k steps at a time."""
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(k, i) + 1):
            dp[i] += dp[i - j]
    return dp[n]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(climbing_stairs(n))


if __name__ == "__main__":
    main()
