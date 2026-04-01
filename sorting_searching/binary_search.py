# Binary Search (Classic + Variations)
# Classic: find target in sorted array.
# Lower bound: first index where arr[i] >= target.
# Upper bound: first index where arr[i] > target.
# Time Complexity: O(log n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n and target
#     Line 2: n space-separated sorted integers
# Output: "classic: idx, lower_bound: idx, upper_bound: idx" per test case

import sys
input = sys.stdin.readline


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(arr, target):
    """First index where arr[i] >= target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr, target):
    """First index where arr[i] > target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main():
    t = int(input())
    for _ in range(t):
        n, target = map(int, input().split())
        arr = list(map(int, input().split()))
        c = binary_search(arr, target)
        lb = lower_bound(arr, target)
        ub = upper_bound(arr, target)
        print(f"classic: {c}, lower_bound: {lb}, upper_bound: {ub}")


if __name__ == "__main__":
    main()
