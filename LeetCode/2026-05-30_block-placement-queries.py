from typing import List
from bisect import bisect_right

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0] * (4 * n)

    def build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        m = (l + r) // 2
        self.build(idx * 2, l, m, arr)
        self.build(idx * 2 + 1, m + 1, r, arr)
        self.seg[idx] = max(self.seg[idx * 2], self.seg[idx * 2 + 1])

    def update(self, idx, l, r, pos, val):
        if l == r:
            self.seg[idx] = val
            return
        m = (l + r) // 2
        if pos <= m:
            self.update(idx * 2, l, m, pos, val)
        else:
            self.update(idx * 2 + 1, m + 1, r, pos, val)
        self.seg[idx] = max(self.seg[idx * 2], self.seg[idx * 2 + 1])

    def query(self, idx, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.seg[idx]
        m = (l + r) // 2
        return max(
            self.query(idx * 2, l, m, ql, qr),
            self.query(idx * 2 + 1, m + 1, r, ql, qr)
        )

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = {0}
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        obs = sorted(obstacles)
        m = len(obs)
        pos_to_idx = {x: i for i, x in enumerate(obs)}

        vals = [0] * m
        for i in range(1, m):
            vals[i] = obs[i] - obs[i - 1]

        seg = SegmentTree(m)
        seg.build(1, 0, m - 1, vals)

        prev = [i - 1 for i in range(m)]
        nxt = [i + 1 for i in range(m)]
        nxt[m - 1] = m

        parent = list(range(m))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        ans = []

        for q in reversed(queries):
            if q[0] == 2:
                _, x, sz = q
                k = bisect_right(obs, x) - 1
                p = find(k)

                best = seg.query(1, 0, m - 1, 0, p)
                best = max(best, x - obs[p])

                ans.append(best >= sz)
            else:
                p = pos_to_idx[q[1]]

                l = prev[p]
                r = nxt[p]

                seg.update(1, 0, m - 1, p, 0)

                if r < m:
                    seg.update(1, 0, m - 1, r, obs[r] - obs[l])
                    prev[r] = l

                if l >= 0:
                    nxt[l] = r

                parent[p] = find(p - 1)

        return ans[::-1]