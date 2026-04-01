# Combination Sum
# Given an array of distinct positive integers (candidates) and a target,
# find all unique combinations where the candidates sum to target.
# Each candidate may be used unlimited times.
# Time Complexity: O(n^(target/min)) | Space Complexity: O(target/min) recursion depth
#
# Also includes Combination Sum II (each candidate used at most once, input may have duplicates).
#
# Input format:
#   Line 1: "1" or "2" (which variant)
#   Line 2: n and target
#   Line 3: n space-separated integers (candidates)
# Output: all unique combinations, one per line, followed by total count

import sys
input = sys.stdin.readline


def combination_sum(candidates, target):
    """Each candidate can be used unlimited times."""
    candidates.sort()
    result = []

    def backtrack(start, remaining, current):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            current.append(candidates[i])
            backtrack(i, remaining - candidates[i], current)  # i, not i+1: reuse allowed
            current.pop()

    backtrack(0, target, [])
    return result


def combination_sum_2(candidates, target):
    """Each candidate used at most once, skip duplicates."""
    candidates.sort()
    result = []

    def backtrack(start, remaining, current):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], current)
            current.pop()

    backtrack(0, target, [])
    return result


def main():
    variant = input().strip()
    n, target = map(int, input().split())
    candidates = list(map(int, input().split()))

    if variant == "1":
        result = combination_sum(candidates, target)
    else:
        result = combination_sum_2(candidates, target)

    for combo in result:
        print(*combo)
    print(f"Total: {len(result)}")


if __name__ == "__main__":
    main()
