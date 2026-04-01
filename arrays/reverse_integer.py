# Reverse Integer
# Reverse the digits of a 32-bit signed integer. Return 0 on overflow.
# Time Complexity: O(log x) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: one integer x per line
# Output: reversed integer per line

import sys
input = sys.stdin.readline

INT_MIN, INT_MAX = -(2**31), 2**31 - 1


def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10
    result *= sign
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        print(reverse_integer(x))


if __name__ == "__main__":
    main()
