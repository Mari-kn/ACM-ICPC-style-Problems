# Minimum Number of Coins (Greedy)
# Given standard coin denominations, find the minimum number of coins to make a given amount.
# Greedy works optimally for canonical coin systems (e.g., 1,5,10,25).
# For arbitrary denominations, use DP (see coin_change.py).
# Time Complexity: O(n) where n = number of denominations | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of denominations), amount
#     Line 2: n space-separated denominations (sorted ascending)
# Output: total coins and breakdown

import sys
input = sys.stdin.readline


def min_coins_greedy(denominations, amount):
    """Greedy: pick largest coin first. Optimal only for canonical systems."""
    coins_used = []
    total = 0
    for coin in reversed(denominations):
        count = amount // coin
        if count > 0:
            coins_used.append((coin, count))
            total += count
            amount -= coin * count
    if amount != 0:
        return -1, []  # greedy failed, need DP
    return total, coins_used


def min_coins_dp(denominations, amount):
    """DP fallback for non-canonical systems. See coin_change.py for full version."""
    INF = float('inf')
    dp = [INF] * (amount + 1)
    parent = [-1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in denominations:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                parent[i] = c

    if dp[amount] == INF:
        return -1, []

    # Reconstruct
    coins_used = {}
    rem = amount
    while rem > 0:
        c = parent[rem]
        coins_used[c] = coins_used.get(c, 0) + 1
        rem -= c

    return dp[amount], sorted(coins_used.items(), reverse=True)


def main():
    t = int(input())
    for _ in range(t):
        n, amount = map(int, input().split())
        denominations = list(map(int, input().split()))

        total_greedy, breakdown_greedy = min_coins_greedy(denominations, amount)
        total_dp, breakdown_dp = min_coins_dp(denominations, amount)

        print(f"greedy: {total_greedy} coins", end="")
        if total_greedy != -1:
            parts = [f"{coin}x{cnt}" for coin, cnt in breakdown_greedy]
            print(f" ({', '.join(parts)})")
        else:
            print(" (failed, use DP)")

        print(f"dp:     {total_dp} coins", end="")
        if total_dp != -1:
            parts = [f"{coin}x{cnt}" for coin, cnt in breakdown_dp]
            print(f" ({', '.join(parts)})")
        else:
            print(" (impossible)")


if __name__ == "__main__":
    main()
