# Matrix Chain Multiplication
# Given dimensions of n matrices, find the optimal parenthesization to minimize
# the total number of scalar multiplications.
# Matrix i has dimensions dims[i] x dims[i+1].
# Time Complexity: O(n^3) | Space Complexity: O(n^2)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n+1 space-separated dimensions (n matrices)
# Output: minimum multiplications and optimal parenthesization

import sys
input = sys.stdin.readline

INF = float('inf')


def matrix_chain(dims):
    """Bottom-up DP with parenthesization reconstruction."""
    n = len(dims) - 1  # number of matrices
    if n <= 0:
        return 0, ""

    # dp[i][j] = min cost to multiply matrices i..j (0-indexed)
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):  # chain length
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = INF
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    def build_parens(i, j):
        if i == j:
            return f"M{i}"
        k = split[i][j]
        left = build_parens(i, k)
        right = build_parens(k + 1, j)
        return f"({left} x {right})"

    return dp[0][n - 1], build_parens(0, n - 1)


def main():
    t = int(input())
    for _ in range(t):
        dims = list(map(int, input().split()))
        cost, parens = matrix_chain(dims)
        print(f"min_cost: {cost}")
        print(f"order: {parens}")


if __name__ == "__main__":
    main()
