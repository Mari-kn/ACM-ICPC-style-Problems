# GCD & LCM (Euclidean Algorithm)
# GCD: Greatest Common Divisor using Euclid's algorithm.
# Extended GCD: also finds coefficients x, y such that ax + by = gcd(a, b).
# LCM: Least Common Multiple via GCD.
# Time Complexity: O(log(min(a, b))) | Space Complexity: O(1) iterative
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: a b
# Output: gcd, lcm, and extended gcd coefficients

import sys
input = sys.stdin.readline


def gcd(a, b):
    """Iterative Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def extended_gcd(a, b):
    """Returns (g, x, y) such that a*x + b*y = g = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def lcm(a, b):
    return a // gcd(a, b) * b  # divide first to avoid overflow


def gcd_multiple(nums):
    """GCD of a list of numbers."""
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd(result, nums[i])
    return result


def lcm_multiple(nums):
    """LCM of a list of numbers."""
    result = nums[0]
    for i in range(1, len(nums)):
        result = lcm(result, nums[i])
    return result


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        g = gcd(a, b)
        l = lcm(a, b)
        eg, x, y = extended_gcd(a, b)
        print(f"gcd({a},{b}) = {g}")
        print(f"lcm({a},{b}) = {l}")
        print(f"extended: {a}*{x} + {b}*{y} = {eg}")


if __name__ == "__main__":
    main()
