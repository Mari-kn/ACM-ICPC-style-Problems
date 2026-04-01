# Prime Numbers (Sieve of Eratosthenes)
# Generate all primes up to n.
# Also includes: primality test, prime factorization, segmented sieve.
# Time Complexity: O(n log log n) for sieve | Space: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n
# Output: count of primes up to n, then the primes

import sys
input = sys.stdin.readline


def sieve_of_eratosthenes(n):
    """Returns list of all primes <= n."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def linear_sieve(n):
    """Linear sieve O(n) — each composite marked exactly once.
    Also computes smallest prime factor (SPF) for fast factorization."""
    spf = [0] * (n + 1)  # smallest prime factor
    primes = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > n:
                break
            spf[i * p] = p
    return primes, spf


def is_prime(n):
    """Trial division O(sqrt(n))."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factorization(n):
    """Trial division factorization O(sqrt(n))."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def factorize_with_spf(n, spf):
    """O(log n) factorization using precomputed smallest prime factors."""
    factors = {}
    while n > 1:
        p = spf[n]
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    return factors


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        primes = sieve_of_eratosthenes(n)
        print(f"count: {len(primes)}")
        if len(primes) <= 100:
            print(*primes)
        else:
            print(*primes[:50], "...", *primes[-10:])


if __name__ == "__main__":
    main()
