# Maximum Subarray (Kadane's Algorithm)
# Find the contiguous subarray with the largest sum.
# Time Complexity: O(n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of elements)
#     Line 2: n space-separated integers
# Output: maximum subarray sum, start index, end index (0-based) per line

import sys
input = sys.stdin.readline


def max_subarray(nums):
    best_sum = nums[0]
    curr_sum = nums[0]
    best_start = best_end = 0
    curr_start = 0
    for i in range(1, len(nums)):
        if curr_sum + nums[i] < nums[i]:
            curr_sum = nums[i]
            curr_start = i
        else:
            curr_sum += nums[i]
        if curr_sum > best_sum:
            best_sum = curr_sum
            best_start = curr_start
            best_end = i
    return best_sum, best_start, best_end


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        total, start, end = max_subarray(nums)
        print(total, start, end)


if __name__ == "__main__":
    main()
