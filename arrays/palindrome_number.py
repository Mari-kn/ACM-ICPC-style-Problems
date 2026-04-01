# Palindrome Number
# Determine whether an integer is a palindrome without converting to string.
# Time Complexity: O(log n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: one integer x per line
# Output: "True" or "False" per line

import sys
input = sys.stdin.readline


def is_palindrome(x):
    # Negative numbers and multiples of 10 (except 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    # Even length: x == reversed_half
    # Odd length: x == reversed_half // 10 (middle digit ignored)
    return x == reversed_half or x == reversed_half // 10


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        print(is_palindrome(x))


if __name__ == "__main__":
    main()
