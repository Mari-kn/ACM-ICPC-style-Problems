# Largest Rectangle in Histogram
# Given an array of bar heights, find the area of the largest rectangle in the histogram.
# Uses a monotonic increasing stack.
# Time Complexity: O(n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of bars)
#     Line 2: n space-separated heights
# Output: largest rectangle area per line

import sys
input = sys.stdin.readline


def largest_rectangle(heights):
    stack = []  # stores indices of increasing heights
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        # Use 0 as sentinel to flush remaining bars
        curr_height = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > curr_height:
            h = heights[stack.pop()]
            # Width extends from (stack top + 1) to (i - 1)
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        heights = list(map(int, input().split()))
        print(largest_rectangle(heights))


if __name__ == "__main__":
    main()
