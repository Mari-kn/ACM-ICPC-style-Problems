# Generate All Subsets (Power Set)
# Given n distinct integers, generate all possible subsets.
# Two approaches: backtracking and bitmasking.
# Time Complexity: O(n * 2^n) | Space Complexity: O(n) recursion depth
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of elements)
#     Line 2: n space-separated integers
# Output: all subsets (empty set shown as "empty"), one per line, followed by total count

import sys
input = sys.stdin.readline


def subsets_backtrack(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


def subsets_bitmask(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)
    return result


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        result = subsets_backtrack(nums)
        for subset in result:
            if subset:
                print(*subset)
            else:
                print("empty")
        print(f"Total: {len(result)}")


if __name__ == "__main__":
    main()
