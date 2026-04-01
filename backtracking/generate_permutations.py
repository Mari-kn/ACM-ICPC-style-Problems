# Generate All Permutations
# Given n distinct integers, generate all possible permutations.
# Uses backtracking with in-place swapping.
# Time Complexity: O(n * n!) | Space Complexity: O(n) recursion depth
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of elements)
#     Line 2: n space-separated integers
# Output: all permutations, one per line, followed by total count

import sys
input = sys.stdin.readline


def permutations(nums):
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        result = permutations(nums)
        for perm in result:
            print(*perm)
        print(f"Total: {len(result)}")


if __name__ == "__main__":
    main()
