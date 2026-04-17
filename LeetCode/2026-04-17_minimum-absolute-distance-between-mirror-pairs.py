from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            return int(str(x)[::-1])
        
        pos = {}
        ans = float('inf')
        
        for i, x in enumerate(nums):
            # Check if current matches reverse of previous numbers
            if x in pos:
                ans = min(ans, i - pos[x])
            
            rev = reverse(x)
            pos[rev] = i  # store reversed value
        
        return ans if ans != float('inf') else -1