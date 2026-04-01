# Valid Parentheses
# Given a string of brackets, determine if the input is valid.
# A string is valid if every open bracket is closed by the same type in correct order.
# Time Complexity: O(n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: one string of brackets per line
# Output: "True" or "False" per line

import sys
input = sys.stdin.readline


def is_valid(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(is_valid(s))


if __name__ == "__main__":
    main()
