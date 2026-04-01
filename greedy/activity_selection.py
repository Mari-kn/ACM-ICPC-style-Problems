# Activity Selection
# Given n activities with start and finish times, select the maximum number
# of non-overlapping activities.
# Greedy: sort by finish time, always pick the earliest finishing compatible activity.
# Time Complexity: O(n log n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of activities)
#     Next n lines: start finish
# Output: max activities count and the selected activities (0-indexed)

import sys
input = sys.stdin.readline


def activity_selection(activities):
    """Greedy by earliest finish time."""
    n = len(activities)
    # Sort by finish time, keeping original indices
    indexed = sorted(range(n), key=lambda i: activities[i][1])

    selected = [indexed[0]]
    last_finish = activities[indexed[0]][1]

    for i in range(1, n):
        idx = indexed[i]
        if activities[idx][0] >= last_finish:
            selected.append(idx)
            last_finish = activities[idx][1]

    return selected


def activity_selection_weighted(activities, weights):
    """Weighted variant: maximize total weight using DP + binary search.
    Time: O(n log n) | Space: O(n)"""
    from bisect import bisect_right

    n = len(activities)
    # Sort by finish time
    order = sorted(range(n), key=lambda i: activities[i][1])
    finishes = [activities[order[i]][1] for i in range(n)]

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        idx = order[i - 1]
        start = activities[idx][0]
        # Find last activity that finishes <= start
        j = bisect_right(finishes, start, 0, i - 1)
        dp[i] = max(dp[i - 1], dp[j] + weights[idx])

    return dp[n]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        activities = []
        for _ in range(n):
            s, f = map(int, input().split())
            activities.append((s, f))
        selected = activity_selection(activities)
        print(f"count: {len(selected)}")
        print("selected:", *sorted(selected))


if __name__ == "__main__":
    main()
