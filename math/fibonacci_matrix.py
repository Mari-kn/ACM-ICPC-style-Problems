# Fibonacci using Matrix Exponentiation
# Compute the nth Fibonacci number in O(log n) using:
#   | F(n+1)  F(n)  |   | 1 1 |^n
#   | F(n)  F(n-1)  | = | 1 0 |
#
# Handles very large n with modular arithmetic.
# Time Complexity: O(log n) with 2x2 matrix mult | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   Next t lines: n mod
# Output: F(n) % mod per line

import sys
input = sys.stdin.readline


def mat_mult_2x2(A, B, mod):
    """Multiply two 2x2 matrices under mod."""
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod],
    ]


def mat_pow_2x2(M, exp, mod):
    """2x2 matrix exponentiation — O(log exp)."""
    result = [[1, 0], [0, 1]]  # identity
    while exp > 0:
        if exp & 1:
            result = mat_mult_2x2(result, M, mod)
        M = mat_mult_2x2(M, M, mod)
        exp >>= 1
    return result


def fib_matrix(n, mod):
    """F(n) mod m in O(log n)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1 % mod
    base = [[1, 1], [1, 0]]
    result = mat_pow_2x2(base, n - 1, mod)
    return result[0][0]


def fib_matrix_no_mod(n):
    """Exact F(n) without modulus using Python big integers."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    def mult(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]],
        ]

    def power(M, exp):
        result = [[1, 0], [0, 1]]
        while exp > 0:
            if exp & 1:
                result = mult(result, M)
            M = mult(M, M)
            exp >>= 1
        return result

    return power([[1, 1], [1, 0]], n - 1)[0][0]


def fib_fast_doubling(n, mod):
    """Fast doubling method — O(log n), constant extra space.
    F(2k)   = F(k) * [2*F(k+1) - F(k)]
    F(2k+1) = F(k)^2 + F(k+1)^2"""
    def helper(n):
        if n == 0:
            return 0, 1
        a, b = helper(n >> 1)
        c = a * ((2 * b - a) % mod) % mod
        d = (a * a + b * b) % mod
        if n & 1:
            return d, (c + d) % mod
        return c, d

    return helper(n)[0]


def main():
    t = int(input())
    for _ in range(t):
        n, mod = map(int, input().split())
        mat = fib_matrix(n, mod)
        dbl = fib_fast_doubling(n, mod)
        print(f"matrix: {mat}, fast_doubling: {dbl}")


if __name__ == "__main__":
    main()
