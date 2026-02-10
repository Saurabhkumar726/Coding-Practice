from typing import List
from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        for l in range(n):
            freq = defaultdict(int)
            even = odd = 0
            
            for r in range(l, n):
                x = nums[r]
                
                if freq[x] == 0:
                    if x % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                
                freq[x] += 1
                
                if even == odd:
                    ans = max(ans, r - l + 1)
        
        return ans
