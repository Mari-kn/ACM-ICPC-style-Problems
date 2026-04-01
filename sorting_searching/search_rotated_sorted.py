# Search in Rotated Sorted Array
# A sorted array is rotated at some pivot. Search for a target in O(log n).
# Also includes finding the rotation pivot (minimum element).
# Time Complexity: O(log n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n and target
#     Line 2: n space-separated integers (rotated sorted, distinct)
# Output: "index: idx, pivot: idx" per line (-1 if target not found)

import sys
input = sys.stdin.readline


def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def find_pivot(nums):
    """Find the index of the minimum element (rotation pivot)."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_rotated_with_duplicates(nums, target):
    """Handles duplicate elements — worst case O(n)."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        # Cannot determine sorted half — shrink
        if nums[lo] == nums[mid] == nums[hi]:
            lo += 1
            hi -= 1
        elif nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def main():
    t = int(input())
    for _ in range(t):
        n, target = map(int, input().split())
        nums = list(map(int, input().split()))
        idx = search_rotated(nums, target)
        pivot = find_pivot(nums)
        print(f"index: {idx}, pivot: {pivot}")


if __name__ == "__main__":
    main()
