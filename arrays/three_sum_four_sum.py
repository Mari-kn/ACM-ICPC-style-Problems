# 3Sum / 4Sum
# 3Sum: Find all unique triplets that sum to zero. O(n^2)
# 4Sum: Find all unique quadruplets that sum to target. O(n^3)
# Both use sorting + two-pointer technique to avoid duplicates.
#
# Input format:
#   Line 1: "3" or "4" (which problem to solve)
#   Line 2: n and target (for 4Sum; target is 0 for 3Sum)
#   Line 3: n space-separated integers
# Output: unique tuples, one per line

import sys
input = sys.stdin.readline


def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result


def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
    return result


def main():
    mode = input().strip()
    parts = list(map(int, input().split()))
    n, target = parts[0], parts[1]
    nums = list(map(int, input().split()))

    if mode == "3":
        for triplet in three_sum(nums):
            print(*triplet)
    else:
        for quad in four_sum(nums, target):
            print(*quad)


if __name__ == "__main__":
    main()
