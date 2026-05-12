import math

class Solution:
    def RangeLCMQuery(self, arr, queries):
        n = len(arr)
        seg = [1] * (4 * n)
        
        def lcm(a, b):
            return (a * b) // math.gcd(a, b)
        
        def build(node, l, r):
            if l == r:
                seg[node] = arr[l]
                return
            
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            seg[node] = lcm(seg[2 * node], seg[2 * node + 1])
        
        def update(node, l, r, idx, val):
            if l == r:
                seg[node] = val
                return
            
            mid = (l + r) // 2
            
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
            
            seg[node] = lcm(seg[2 * node], seg[2 * node + 1])
        
        def query(node, l, r, ql, qr):
            if qr < l or ql > r:
                return 1
            
            if ql <= l and r <= qr:
                return seg[node]
            
            mid = (l + r) // 2
            
            left = query(2 * node, l, mid, ql, qr)
            right = query(2 * node + 1, mid + 1, r, ql, qr)
            
            return lcm(left, right)
        
        build(1, 0, n - 1)
        
        ans = []
        
        for q in queries:
            if q[0] == 1:
                _, idx, val = q
                update(1, 0, n - 1, idx, val)
            else:
                _, l, r = q
                ans.append(query(1, 0, n - 1, l, r))
        
        return ans