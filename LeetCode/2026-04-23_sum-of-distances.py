from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        res = [0] * len(nums)
        
        for indices in pos.values():
            k = len(indices)
            if k == 1:
                continue
            
            prefix = [0] * k
            prefix[0] = indices[0]
            
            for i in range(1, k):
                prefix[i] = prefix[i - 1] + indices[i]
            
            for i in range(k):
                idx = indices[i]
                
                left = i * idx - (prefix[i - 1] if i > 0 else 0)
                right = (prefix[k - 1] - prefix[i]) - (k - i - 1) * idx
                
                res[idx] = left + right
        
        return res
        