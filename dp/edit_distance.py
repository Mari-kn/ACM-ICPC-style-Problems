# Edit Distance (Levenshtein Distance)
# Minimum number of insertions, deletions, and substitutions to transform s1 into s2.
# Time Complexity: O(n * m) | Space Complexity: O(min(n, m)) optimized
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: string s1
#     Line 2: string s2
# Output: edit distance and the sequence of operations

import sys
input = sys.stdin.readline


def edit_distance_full(s1, s2):
    """Full DP table with operation reconstruction."""
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete
                    dp[i][j - 1],      # insert
                    dp[i - 1][j - 1],  # replace
                )

    # Reconstruct operations
    ops = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            ops.append(f"keep '{s1[i - 1]}'")
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            ops.append(f"replace '{s1[i - 1]}' -> '{s2[j - 1]}'")
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            ops.append(f"insert '{s2[j - 1]}'")
            j -= 1
        else:
            ops.append(f"delete '{s1[i - 1]}'")
            i -= 1

    return dp[n][m], ops[::-1]


def edit_distance_optimized(s1, s2):
    """O(min(n, m)) space — distance only."""
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    n, m = len(s1), len(s2)
    prev = list(range(m + 1))
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        curr[0] = i
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, [0] * (m + 1)

    return prev[m]


def main():
    t = int(input())
    for _ in range(t):
        s1 = input().strip()
        s2 = input().strip()
        dist, ops = edit_distance_full(s1, s2)
        print(f"distance: {dist}")
        print("operations:", " | ".join(ops))


if __name__ == "__main__":
    main()
