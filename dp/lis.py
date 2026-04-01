# Longest Increasing Subsequence (LIS)
# Approach 1: DP — O(n^2) time, O(n) space.
# Approach 2: Patience sorting with binary search — O(n log n) time, O(n) space.
# Both reconstruct the actual subsequence.
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n
#     Line 2: n space-separated integers
# Output: LIS length and the subsequence itself

import sys
from bisect import bisect_left
input = sys.stdin.readline


def lis_dp(nums):
    """O(n^2) DP with reconstruction."""
    n = len(nums)
    if n == 0:
        return 0, []
    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    length = max(dp)
    idx = dp.index(length)
    seq = []
    while idx != -1:
        seq.append(nums[idx])
        idx = parent[idx]
    return length, seq[::-1]


def lis_binary_search(nums):
    """O(n log n) patience sorting with reconstruction."""
    n = len(nums)
    if n == 0:
        return 0, []

    tails = []       # tails[i] = smallest tail element for LIS of length i+1
    indices = []     # indices[i] = index in nums of tails[i]
    parent = [-1] * n

    for i, num in enumerate(nums):
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
            indices.append(i)
        else:
            tails[pos] = num
            indices[pos] = i
        if pos > 0:
            parent[i] = indices[pos - 1]

    length = len(tails)
    seq = []
    idx = indices[-1]
    while idx != -1:
        seq.append(nums[idx])
        idx = parent[idx]
    return length, seq[::-1]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        length, seq = lis_binary_search(nums)
        print(f"length: {length}")
        print("LIS:", *seq)


if __name__ == "__main__":
    main()
