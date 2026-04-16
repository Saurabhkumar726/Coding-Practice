from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        ans = []
        
        for q in queries:
            v = nums[q]
            lst = pos[v]
            
            if len(lst) == 1:
                ans.append(-1)
                continue
            
            i = bisect.bisect_left(lst, q)
            
            left = lst[i - 1] if i > 0 else lst[-1]
            right = lst[i + 1] if i < len(lst) - 1 else lst[0]
            
            d1 = abs(q - left)
            d1 = min(d1, n - d1)
            
            d2 = abs(q - right)
            d2 = min(d2, n - d2)
            
            ans.append(min(d1, d2))
        
        return ans