# Find Kth Largest Element
# Three approaches:
#   1. Quickselect (Hoare's) — Average O(n), Worst O(n^2)
#   2. Min-heap of size k — O(n log k)
#   3. Sort — O(n log n) baseline
# Space: O(1) for quickselect, O(k) for heap
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n and k
#     Line 2: n space-separated integers
# Output: kth largest element per line

import sys
import random
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def quickselect(arr, lo, hi, k):
    """Find kth smallest element (0-indexed) using randomized partition."""
    if lo == hi:
        return arr[lo]
    pivot_idx = random.randint(lo, hi)
    arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
    pivot = arr[hi]
    store = lo
    for i in range(lo, hi):
        if arr[i] <= pivot:
            arr[store], arr[i] = arr[i], arr[store]
            store += 1
    arr[store], arr[hi] = arr[hi], arr[store]

    if store == k:
        return arr[store]
    elif store < k:
        return quickselect(arr, store + 1, hi, k)
    else:
        return quickselect(arr, lo, store - 1, k)


def kth_largest_quickselect(nums, k):
    """Kth largest = (n-k)th smallest."""
    n = len(nums)
    return quickselect(nums, 0, n - 1, n - k)


def kth_largest_heap(nums, k):
    """Maintain a min-heap of size k."""
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        # Using quickselect (make a copy since it modifies array)
        result_qs = kth_largest_quickselect(nums[:], k)
        result_hp = kth_largest_heap(nums, k)
        print(f"quickselect: {result_qs}, heap: {result_hp}")


if __name__ == "__main__":
    main()
