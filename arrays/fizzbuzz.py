# FizzBuzz
# Print numbers 1 to n, replacing multiples of 3 with "Fizz",
# multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
# Time Complexity: O(n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: integer n
# Output: one result per line

import sys
input = sys.stdin.readline


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def main():
    n = int(input())
    fizzbuzz(n)


if __name__ == "__main__":
    main()
