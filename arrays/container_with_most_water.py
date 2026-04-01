# Container With Most Water
# Given n vertical lines, find two lines that together with the x-axis form a container
# holding the most water. Two-pointer greedy approach.
# Time Complexity: O(n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of lines)
#     Line 2: n space-separated heights
# Output: maximum water area per line

import sys
input = sys.stdin.readline


def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        best = max(best, w * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        print(max_area(height))


if __name__ == "__main__":
    main()
