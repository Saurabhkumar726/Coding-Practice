from typing import List

fmin = lambda x, y: x if x < y else y
fmax = lambda x, y: x if x > y else y
INF = 10 ** 20


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.minv = [0] * (4 * self.n)
        self.maxv = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, node, l, r, arr):
        if l == r:
            self.minv[node] = arr[l]
            self.maxv[node] = arr[l]
            return
        mid = (l + r) // 2
        self._build(node * 2, l, mid, arr)
        self._build(node * 2 + 1, mid + 1, r, arr)
        self._pull(node)

    def _pull(self, node):
        self.minv[node] = fmin(self.minv[node * 2], self.minv[node * 2 + 1])
        self.maxv[node] = fmax(self.maxv[node * 2], self.maxv[node * 2 + 1])

    def _apply(self, node, val):
        self.minv[node] += val
        self.maxv[node] += val
        self.lazy[node] += val

    def _push(self, node):
        if self.lazy[node] != 0:
            self._apply(node * 2, self.lazy[node])
            self._apply(node * 2 + 1, self.lazy[node])
            self.lazy[node] = 0

    def range_add(self, ql, qr, val, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or ql > r:
            return
        if ql <= l and r <= qr:
            self._apply(node, val)
            return
        self._push(node)
        mid = (l + r) // 2
        self.range_add(ql, qr, val, node * 2, l, mid)
        self.range_add(ql, qr, val, node * 2 + 1, mid + 1, r)
        self._pull(node)

    def walk(self, ql, qr, node=1, l=0, r=None, t=None):
        if r is None:
            r = self.n - 1
        if qr < l or ql > r:
            return INF

        if t < self.minv[node] or t > self.maxv[node]:
            return INF

        if l == r:
            return l

        self._push(node)
        mid = (l + r) // 2

        if self.minv[node * 2] <= t <= self.maxv[node * 2]:
            return self.walk(ql, fmin(qr, mid), node * 2, l, mid, t)
        return self.walk(fmax(ql, mid + 1), qr, node * 2 + 1, mid + 1, r, t)

    def get(self, idx, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            return self.minv[node]
        self._push(node)
        mid = (l + r) // 2
        if idx <= mid:
            return self.get(idx, node * 2, l, mid)
        else:
            return self.get(idx, node * 2 + 1, mid + 1, r)

    def d(self):
        for i in range(self.n):
            print(self.get(i), end=" ")
        print()


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)

        st = SegmentTree([0] * N)
        current = 0

        last = {}
        best = 0

        for index, x in enumerate(nums):
            delta = 1
            if x % 2 == 1:
                delta = -delta

            if x in last:
                st.range_add(last[x], index - 1, -delta)

            last[x] = index

            if index > 0:
                current = st.get(index - 1)
            current += delta

            if current == 0:
                best = max(best, index + 1)
            else:
                prev = st.walk(0, index - 1, 1, 0, N - 1, current)
                if prev != INF:
                    best = max(best, index - prev)

            st.range_add(index, index, current)

        return best