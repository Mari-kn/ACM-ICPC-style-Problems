# Fast Exponentiation (Binary Exponentiation)
# Compute base^exp in O(log exp) using repeated squaring.
# Works for integers, modular arithmetic, and matrix exponentiation.
# Time Complexity: O(log exp) | Space Complexity: O(1) iterative
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: base exp mod
# Output: (base^exp) % mod per line

import sys
input = sys.stdin.readline


def fast_pow_iterative(base, exp, mod):
    """Iterative binary exponentiation — O(log exp)."""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result


def fast_pow_recursive(base, exp, mod):
    """Recursive binary exponentiation — O(log exp)."""
    if exp == 0:
        return 1
    if exp & 1:
        return base * fast_pow_recursive(base, exp - 1, mod) % mod
    half = fast_pow_recursive(base, exp >> 1, mod)
    return half * half % mod


def fast_pow_no_mod(base, exp):
    """Without modulus — for arbitrary precision integers."""
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result


def matrix_mult(A, B, mod):
    """Multiply two n x n matrices under mod."""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C


def matrix_pow(M, exp, mod):
    """Matrix exponentiation — O(n^3 * log exp)."""
    n = len(M)
    # Identity matrix
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while exp > 0:
        if exp & 1:
            result = matrix_mult(result, M, mod)
        M = matrix_mult(M, M, mod)
        exp >>= 1
    return result


def main():
    t = int(input())
    for _ in range(t):
        base, exp, mod = map(int, input().split())
        it = fast_pow_iterative(base, exp, mod)
        rec = fast_pow_recursive(base, exp, mod)
        print(f"iterative: {it}, recursive: {rec}")


if __name__ == "__main__":
    main()
