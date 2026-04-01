# String Compression
# Compress a string using counts of repeated characters.
# "aabcccccaaa" -> "a2b1c5a3". Return original if compressed is not shorter.
# Time Complexity: O(n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: one string per line
# Output: compressed string (or original if not shorter) per line

import sys
input = sys.stdin.readline


def compress(s):
    if not s:
        return s
    parts = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            parts.append(s[i - 1])
            parts.append(str(count))
            count = 1
    parts.append(s[-1])
    parts.append(str(count))
    compressed = "".join(parts)
    return compressed if len(compressed) < len(s) else s


def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(compress(s))


if __name__ == "__main__":
    main()
