# Gas Station Problem
# There are n gas stations on a circular route. Station i has gas[i] fuel
# and costs cost[i] to travel to station i+1. Find the starting station
# index to complete the full circuit, or -1 if impossible.
# Greedy: if total gas >= total cost, a solution exists. Track the running
# surplus and reset start whenever it goes negative.
# Time Complexity: O(n) | Space Complexity: O(1)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of stations)
#     Line 2: n space-separated gas values
#     Line 3: n space-separated cost values
# Output: starting station index (0-indexed) or -1

import sys
input = sys.stdin.readline


def can_complete_circuit(gas, cost):
    total_surplus = 0
    current_surplus = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_surplus += diff
        current_surplus += diff
        if current_surplus < 0:
            # Cannot start from any station before i+1
            start = i + 1
            current_surplus = 0

    return start if total_surplus >= 0 else -1


def can_complete_circuit_bruteforce(gas, cost):
    """O(n^2) brute force for verification."""
    n = len(gas)
    for start in range(n):
        tank = 0
        valid = True
        for j in range(n):
            idx = (start + j) % n
            tank += gas[idx] - cost[idx]
            if tank < 0:
                valid = False
                break
        if valid:
            return start
    return -1


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        gas = list(map(int, input().split()))
        cost = list(map(int, input().split()))
        result = can_complete_circuit(gas, cost)
        if result == -1:
            print(-1)
        else:
            print(f"start: {result}")


if __name__ == "__main__":
    main()
