# Move Zeroes
# Move all zeroes to the end of the array while maintaining relative order of non-zero elements.
# Time Complexity: O(n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of elements)
#     Line 2: n space-separated integers
# Output: modified array per line

import sys
input = sys.stdin.readline


def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        move_zeroes(nums)
        print(*nums)


if __name__ == "__main__":
    main()
