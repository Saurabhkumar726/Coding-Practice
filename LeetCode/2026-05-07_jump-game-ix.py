from typing import List
from bisect import bisect_right

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        vals = sorted(set(nums))
        m = len(vals)
        
        seg = [10**18] * (4 * m)
        
        def update(node, l, r, idx, val):
            if l == r:
                seg[node] = min(seg[node], val)
                return
            
            mid = (l + r) // 2
            
            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)
            
            seg[node] = min(seg[node * 2], seg[node * 2 + 1])
        
        def query(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 10**18
            
            if ql <= l and r <= qr:
                return seg[node]
            
            mid = (l + r) // 2
            
            return min(
                query(node * 2, l, mid, ql, qr),
                query(node * 2 + 1, mid + 1, r, ql, qr)
            )
        
        intervals = []
        
        for j, x in enumerate(nums):
            idx = bisect_right(vals, x)
            
            if idx < m:
                left = query(1, 0, m - 1, idx, m - 1)
                
                if left != 10**18:
                    intervals.append([left, j])
            
            pos = bisect_right(vals, x) - 1
            update(1, 0, m - 1, pos, j)
        
        if not intervals:
            return nums[:]
        
        intervals.sort()
        
        merged = []
        l, r = intervals[0]
        
        for a, b in intervals[1:]:
            if a <= r:
                r = max(r, b)
            else:
                merged.append([l, r])
                l, r = a, b
        
        merged.append([l, r])
        
        ans = nums[:]
        
        for l, r in merged:
            mx = max(nums[l:r + 1])
            for i in range(l, r + 1):
                ans[i] = mx
        
        return ans