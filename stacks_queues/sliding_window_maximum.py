# Sliding Window Maximum
# Given an array and window size k, find the maximum in each sliding window.
# Uses a monotonic decreasing deque.
# Time Complexity: O(n) | Space Complexity: O(k)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n and k
#     Line 2: n space-separated integers
# Output: space-separated maximums per line

import sys
from collections import deque
input = sys.stdin.readline


def max_sliding_window(nums, k):
    dq = deque()  # stores indices, front is always the max
    result = []
    for i in range(len(nums)):
        # Remove elements outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements from the back
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        # Window is fully formed
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        print(*max_sliding_window(nums, k))


if __name__ == "__main__":
    main()
