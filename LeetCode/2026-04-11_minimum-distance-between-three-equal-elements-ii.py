from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        ans = float('inf')
        
        for idxs in pos.values():
            if len(idxs) < 3:
                continue
            
            for i in range(len(idxs) - 2):
                a, b, c = idxs[i], idxs[i + 1], idxs[i + 2]
                dist = 2 * (c - a)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1