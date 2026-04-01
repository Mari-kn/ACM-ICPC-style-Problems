# Two Sum
# Given an array of integers and a target, find two indices such that they add up to the target.
# Time Complexity: O(n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: n (number of elements), target
#   Line 2: n space-separated integers
# Output: two 0-based indices

import sys
input = sys.stdin.readline


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return -1, -1


def main():
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))
    i, j = two_sum(nums, target)
    print(i, j)


if __name__ == "__main__":
    main()
