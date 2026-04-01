# Rabin-Karp Algorithm
# Rolling hash based pattern matching. Useful for multi-pattern search.
# Average Time: O(n + m) | Worst Time: O(nm) on hash collisions | Space: O(1)
#   where n = len(text), m = len(pattern)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: text
#     Line 2: pattern
# Output: space-separated 0-based indices of all matches, or -1 if none

import sys
input = sys.stdin.readline

BASE = 256
MOD = 10**9 + 7


def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    if m == 0:
        return []

    # Precompute BASE^(m-1) % MOD
    h = pow(BASE, m - 1, MOD)

    # Compute initial hashes
    p_hash = 0
    t_hash = 0
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD

    matches = []
    for i in range(n - m + 1):
        if p_hash == t_hash:
            # Verify character by character to handle collisions
            if text[i:i + m] == pattern:
                matches.append(i)
        # Roll the hash: remove leading char, add trailing char
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * h) * BASE + ord(text[i + m])) % MOD
    return matches


def main():
    t = int(input())
    for _ in range(t):
        text = input().strip()
        pattern = input().strip()
        matches = rabin_karp(text, pattern)
        if matches:
            print(*matches)
        else:
            print(-1)


if __name__ == "__main__":
    main()
