from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        ans = float('inf')
        
        for v in pos:
            idxs = pos[v]
            m = len(idxs)
            if m < 3:
                continue
            
            for i in range(m - 2):
                a, b, c = idxs[i], idxs[i + 1], idxs[i + 2]
                dist = abs(a - b) + abs(b - c) + abs(c - a)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1