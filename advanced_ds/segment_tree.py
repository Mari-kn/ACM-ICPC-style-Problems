# Segment Tree
# Supports range queries and point/range updates in O(log n).
# Implementations: basic (point update + range query), lazy propagation (range update).
# Time Complexity: O(log n) per query/update | Space: O(n)
#
# Input format:
#   Line 1: n (array size), q (queries)
#   Line 2: n space-separated integers (initial array)
#   Next q lines: one of:
#     query l r        (sum of arr[l..r], 0-indexed inclusive)
#     update i val     (set arr[i] = val)
#     range_add l r val (add val to arr[l..r])
#     range_query l r  (sum of arr[l..r] with lazy propagation)
# Output: result of query operations

import sys
input = sys.stdin.readline


class SegmentTree:
    """Point update, range sum query."""
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, lo, hi):
        if lo == hi:
            self.tree[node] = data[lo]
            return
        mid = (lo + hi) // 2
        self._build(data, 2 * node, lo, mid)
        self._build(data, 2 * node + 1, mid + 1, hi)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, idx, val):
        """Set arr[idx] = val."""
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, lo, hi, idx, val):
        if lo == hi:
            self.tree[node] = val
            return
        mid = (lo + hi) // 2
        if idx <= mid:
            self._update(2 * node, lo, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, hi, idx, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l, r):
        """Sum of arr[l..r]."""
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self.tree[node]
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, l, r) +
                self._query(2 * node + 1, mid + 1, hi, l, r))


class LazySegmentTree:
    """Range add update, range sum query with lazy propagation."""
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        if self.n > 0:
            self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, lo, hi):
        if lo == hi:
            self.tree[node] = data[lo]
            return
        mid = (lo + hi) // 2
        self._build(data, 2 * node, lo, mid)
        self._build(data, 2 * node + 1, mid + 1, hi)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push_down(self, node, lo, hi):
        if self.lazy[node] != 0:
            mid = (lo + hi) // 2
            self._apply(2 * node, lo, mid, self.lazy[node])
            self._apply(2 * node + 1, mid + 1, hi, self.lazy[node])
            self.lazy[node] = 0

    def _apply(self, node, lo, hi, val):
        self.tree[node] += val * (hi - lo + 1)
        self.lazy[node] += val

    def range_add(self, l, r, val):
        """Add val to arr[l..r]."""
        self._range_add(1, 0, self.n - 1, l, r, val)

    def _range_add(self, node, lo, hi, l, r, val):
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r:
            self._apply(node, lo, hi, val)
            return
        self._push_down(node, lo, hi)
        mid = (lo + hi) // 2
        self._range_add(2 * node, lo, mid, l, r, val)
        self._range_add(2 * node + 1, mid + 1, hi, l, r, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l, r):
        """Sum of arr[l..r]."""
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self.tree[node]
        self._push_down(node, lo, hi)
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, l, r) +
                self._query(2 * node + 1, mid + 1, hi, l, r))


def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    st = SegmentTree(arr)
    lst = LazySegmentTree(arr)

    for _ in range(q):
        parts = input().split()
        op = parts[0]
        if op == "query":
            l, r = int(parts[1]), int(parts[2])
            print(st.query(l, r))
        elif op == "update":
            i, val = int(parts[1]), int(parts[2])
            st.update(i, val)
        elif op == "range_add":
            l, r, val = int(parts[1]), int(parts[2]), int(parts[3])
            lst.range_add(l, r, val)
        elif op == "range_query":
            l, r = int(parts[1]), int(parts[2])
            print(lst.query(l, r))


if __name__ == "__main__":
    main()
