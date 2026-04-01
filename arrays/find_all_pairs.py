# Find All Pairs with Target Sum
# Given an array of integers and a target, find all unique pairs that sum to the target.
# Time Complexity: O(n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: n (number of elements), target
#   Line 2: n space-separated integers
# Output: all unique pairs, one per line

import sys
input = sys.stdin.readline


def find_all_pairs(nums, target):
    seen = set()
    used = set()
    result = []
    for num in nums:
        complement = target - num
        pair = (min(num, complement), max(num, complement))
        if complement in seen and pair not in used:
            result.append(pair)
            used.add(pair)
        seen.add(num)
    return result


def main():
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))
    pairs = find_all_pairs(nums, target)
    for a, b in pairs:
        print(a, b)


if __name__ == "__main__":
    main()
