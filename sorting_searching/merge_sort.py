# Merge Sort
# Stable, divide-and-conquer sorting algorithm.
# Time Complexity: O(n log n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of elements)
#     Line 2: n space-separated integers
# Output: sorted array per line

import sys
input = sys.stdin.readline


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_inplace(arr, lo, hi):
    """In-place variant using auxiliary buffer."""
    if hi - lo <= 1:
        return
    mid = (lo + hi) // 2
    merge_sort_inplace(arr, lo, mid)
    merge_sort_inplace(arr, mid, hi)
    merged = []
    i, j = lo, mid
    while i < mid and j < hi:
        if arr[i] <= arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1
    merged.extend(arr[i:mid])
    merged.extend(arr[j:hi])
    arr[lo:hi] = merged


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        sorted_arr = merge_sort(arr)
        print(*sorted_arr)


if __name__ == "__main__":
    main()
