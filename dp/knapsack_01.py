# 0/1 Knapsack
# Given n items with weights and values, maximize total value within capacity W.
# Each item can be taken at most once.
# Time Complexity: O(n * W) | Space Complexity: O(W) optimized, O(n * W) with reconstruction
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (items), W (capacity)
#     Next n lines: weight value
# Output: maximum value and selected items

import sys
input = sys.stdin.readline


def knapsack_full(weights, values, W):
    """Full DP table with item reconstruction."""
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]  # skip item i
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # Reconstruct selected items
    selected = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)  # 0-indexed item
            w -= weights[i - 1]

    return dp[n][W], selected[::-1]


def knapsack_optimized(weights, values, W):
    """O(W) space — value only, no reconstruction."""
    n = len(weights)
    dp = [0] * (W + 1)

    for i in range(n):
        # Traverse backwards to avoid using item i twice
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]


def main():
    t = int(input())
    for _ in range(t):
        n, W = map(int, input().split())
        weights = []
        values = []
        for _ in range(n):
            w, v = map(int, input().split())
            weights.append(w)
            values.append(v)
        max_val, selected = knapsack_full(weights, values, W)
        print(f"max_value: {max_val}")
        print(f"items: {' '.join(map(str, selected))}")


if __name__ == "__main__":
    main()
