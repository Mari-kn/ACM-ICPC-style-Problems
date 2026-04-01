# Trapping Rain Water
# Given n non-negative integers representing an elevation map, compute how much water
# it can trap after raining. Two-pointer approach.
# Time Complexity: O(n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of bars)
#     Line 2: n space-separated heights
# Output: total trapped water per line

import sys
input = sys.stdin.readline


def trap(height):
    if len(height) < 3:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    return water


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        print(trap(height))


if __name__ == "__main__":
    main()
