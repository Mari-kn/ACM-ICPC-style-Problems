# Modular Arithmetic
# Common operations under modulus for competitive programming.
# Includes: mod add/sub/mul, modular exponentiation, modular inverse,
# nCr mod p, and Chinese Remainder Theorem.
# All operations assume MOD is prime unless noted otherwise.
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: operation a b mod
#     Operations: "add", "sub", "mul", "pow", "inv", "ncr"
# Output: result per line

import sys
input = sys.stdin.readline

DEFAULT_MOD = 10**9 + 7


def mod_add(a, b, mod=DEFAULT_MOD):
    return (a % mod + b % mod) % mod


def mod_sub(a, b, mod=DEFAULT_MOD):
    return (a % mod - b % mod + mod) % mod


def mod_mul(a, b, mod=DEFAULT_MOD):
    return (a % mod) * (b % mod) % mod


def mod_pow(base, exp, mod=DEFAULT_MOD):
    """Fast modular exponentiation O(log exp)."""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result


def mod_inv(a, mod=DEFAULT_MOD):
    """Modular inverse using Fermat's little theorem (mod must be prime)."""
    return mod_pow(a, mod - 2, mod)


def mod_inv_extended(a, mod):
    """Modular inverse using extended GCD (works for any coprime a, mod)."""
    def ext_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x, y = ext_gcd(b, a % b)
        return g, y, x - (a // b) * y

    g, x, _ = ext_gcd(a % mod, mod)
    if g != 1:
        return -1  # inverse doesn't exist
    return x % mod


class NcrMod:
    """Precompute factorials for nCr mod p queries. O(n) preprocess, O(1) per query."""
    def __init__(self, max_n, mod=DEFAULT_MOD):
        self.mod = mod
        self.fact = [1] * (max_n + 1)
        self.inv_fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.inv_fact[max_n] = mod_pow(self.fact[max_n], mod - 2, mod)
        for i in range(max_n - 1, -1, -1):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % mod

    def ncr(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.inv_fact[r] % self.mod * self.inv_fact[n - r] % self.mod


def chinese_remainder_theorem(remainders, moduli):
    """CRT: solve system x ≡ r_i (mod m_i) for pairwise coprime moduli.
    Returns (solution, product of moduli)."""
    M = 1
    for m in moduli:
        M *= m
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        yi = mod_inv_extended(Mi, m)
        x = (x + r * Mi * yi) % M
    return x, M


def main():
    t = int(input())
    for _ in range(t):
        parts = input().split()
        op = parts[0]
        if op == "add":
            a, b, mod = int(parts[1]), int(parts[2]), int(parts[3])
            print(mod_add(a, b, mod))
        elif op == "sub":
            a, b, mod = int(parts[1]), int(parts[2]), int(parts[3])
            print(mod_sub(a, b, mod))
        elif op == "mul":
            a, b, mod = int(parts[1]), int(parts[2]), int(parts[3])
            print(mod_mul(a, b, mod))
        elif op == "pow":
            base, exp, mod = int(parts[1]), int(parts[2]), int(parts[3])
            print(mod_pow(base, exp, mod))
        elif op == "inv":
            a, mod = int(parts[1]), int(parts[2])
            print(mod_inv(a, mod))
        elif op == "ncr":
            n, r, mod = int(parts[1]), int(parts[2]), int(parts[3])
            comb = NcrMod(n, mod)
            print(comb.ncr(n, r))


if __name__ == "__main__":
    main()
