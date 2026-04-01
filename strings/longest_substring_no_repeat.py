# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
# Sliding window with hash map approach.
# Time Complexity: O(n) | Space Complexity: O(min(n, charset))
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: one string per line
# Output: length of longest substring per line

import sys
input = sys.stdin.readline


def longest_substring(s):
    last_seen = {}
    start = 0
    best = 0
    for end, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = end
        best = max(best, end - start + 1)
    return best


def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(longest_substring(s))


if __name__ == "__main__":
    main()
