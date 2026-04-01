# Longest Palindromic Substring
# Find the longest palindromic substring in a given string.
# Expand-around-center approach (simpler, same optimal complexity as Manacher for practice).
# Time Complexity: O(n^2) | Space Complexity: O(1)
#
# Also includes Manacher's Algorithm for O(n) reference.
# Time Complexity: O(n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: one string per line
# Output: longest palindromic substring per line

import sys
input = sys.stdin.readline


def expand_around_center(s):
    n = len(s)
    if n == 0:
        return ""
    start = end = 0

    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(n):
        # Odd length palindrome
        l1, r1 = expand(i, i)
        if r1 - l1 > end - start:
            start, end = l1, r1
        # Even length palindrome
        l2, r2 = expand(i, i + 1)
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]


def manacher(s):
    """Manacher's Algorithm - O(n) time, O(n) space."""
    if not s:
        return ""
    # Transform: "abc" -> "^#a#b#c#$"
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len = max(p)
    center_idx = p.index(max_len)
    start = (center_idx - max_len) // 2
    return s[start:start + max_len]


def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        # Using expand-around-center (switch to manacher(s) for O(n))
        print(expand_around_center(s))


if __name__ == "__main__":
    main()
