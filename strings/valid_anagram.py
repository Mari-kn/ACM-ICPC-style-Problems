# Valid Anagram
# Given two strings, determine if one is an anagram of the other.
# Time Complexity: O(n) | Space Complexity: O(1) (fixed 26-char alphabet)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: string s
#     Line 2: string t
# Output: "True" or "False" per test case

import sys
input = sys.stdin.readline


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    return all(c == 0 for c in count)


def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        t_str = input().strip()
        print(is_anagram(s, t_str))


if __name__ == "__main__":
    main()
