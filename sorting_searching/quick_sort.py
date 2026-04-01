# Quick Sort
# In-place, divide-and-conquer sorting. Uses Lomuto and Hoare partitioning.
# Average Time: O(n log n) | Worst Time: O(n^2) | Space: O(log n) avg recursion
# Median-of-three pivot selection to reduce worst-case likelihood.
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of elements)
#     Line 2: n space-separated integers
# Output: sorted array per line

import sys
import random
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def quick_sort_lomuto(arr, lo, hi):
    """Lomuto partition scheme."""
    if lo >= hi:
        return
    pivot_idx = median_of_three(arr, lo, hi)
    arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    quick_sort_lomuto(arr, lo, i - 1)
    quick_sort_lomuto(arr, i + 1, hi)


def quick_sort_hoare(arr, lo, hi):
    """Hoare partition scheme — fewer swaps on average."""
    if lo >= hi:
        return
    pivot_idx = median_of_three(arr, lo, hi)
    arr[pivot_idx], arr[lo] = arr[lo], arr[pivot_idx]
    pivot = arr[lo]
    i, j = lo - 1, hi + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    quick_sort_hoare(arr, lo, j)
    quick_sort_hoare(arr, j + 1, hi)


def median_of_three(arr, lo, hi):
    mid = (lo + hi) // 2
    if arr[lo] > arr[mid]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
    if arr[lo] > arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    if arr[mid] > arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
    return mid


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        quick_sort_hoare(arr, 0, n - 1)
        print(*arr)


if __name__ == "__main__":
    main()
