# KMP (Knuth-Morris-Pratt) Pattern Matching
# Search for all occurrences of a pattern in a text using the KMP algorithm.
# Builds a failure/prefix function to skip unnecessary comparisons.
# Time Complexity: O(n + m) | Space Complexity: O(m)
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


def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    lps = build_lps(pattern)
    matches = []
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


def main():
    t = int(input())
    for _ in range(t):
        text = input().strip()
        pattern = input().strip()
        matches = kmp_search(text, pattern)
        if matches:
            print(*matches)
        else:
            print(-1)


if __name__ == "__main__":
    main()
