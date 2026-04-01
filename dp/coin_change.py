# Coin Change
# Given coin denominations and a target amount, find the minimum number of coins needed.
# Also includes counting total number of combinations.
# Time Complexity: O(amount * n) | Space Complexity: O(amount)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of coin types), amount
#     Line 2: n space-separated coin values
# Output: minimum coins needed (-1 if impossible), and number of combinations

import sys
input = sys.stdin.readline

INF = float('inf')


def min_coins(coins, amount):
    """Minimum number of coins to make amount."""
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
    return dp[amount] if dp[amount] != INF else -1


def count_combinations(coins, amount):
    """Number of distinct combinations (order doesn't matter)."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for i in range(c, amount + 1):
            dp[i] += dp[i - c]
    return dp[amount]


def count_permutations(coins, amount):
    """Number of distinct permutations (order matters)."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] += dp[i - c]
    return dp[amount]


def main():
    t = int(input())
    for _ in range(t):
        n, amount = map(int, input().split())
        coins = list(map(int, input().split()))
        mc = min_coins(coins, amount)
        combos = count_combinations(coins, amount)
        print(f"min_coins: {mc}, combinations: {combos}")


if __name__ == "__main__":
    main()
