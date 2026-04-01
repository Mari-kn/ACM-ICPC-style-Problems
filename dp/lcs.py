# Longest Common Subsequence (LCS)
# Find the length and actual LCS of two strings/sequences.
# Time Complexity: O(n * m) | Space Complexity: O(n * m) full, O(min(n,m)) length-only
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: string s1
#     Line 2: string s2
# Output: LCS length and the subsequence

import sys
input = sys.stdin.readline


def lcs_full(s1, s2):
    """Full DP table with reconstruction."""
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct
    seq = []
    i, j = n, m
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            seq.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[n][m], "".join(reversed(seq))


def lcs_space_optimized(s1, s2):
    """O(min(n,m)) space — length only, no reconstruction."""
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    n, m = len(s1), len(s2)
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (m + 1)

    return prev[m]


def main():
    t = int(input())
    for _ in range(t):
        s1 = input().strip()
        s2 = input().strip()
        length, seq = lcs_full(s1, s2)
        print(f"length: {length}")
        print(f"LCS: {seq}")


if __name__ == "__main__":
    main()
