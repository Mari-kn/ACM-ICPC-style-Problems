# Remove Duplicates from Sorted Array
# Given a sorted array, remove duplicates in-place and return the new length.
# Time Complexity: O(n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of elements)
#     Line 2: n space-separated sorted integers
# Output: new length, then the array up to that length

import sys
input = sys.stdin.readline


def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        k = remove_duplicates(nums)
        print(k)
        print(*nums[:k])


if __name__ == "__main__":
    main()
