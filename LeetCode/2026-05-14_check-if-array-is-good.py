from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        
        if len(nums) != n + 1:
            return False
        
        nums.sort()
        
        return nums == list(range(1, n)) + [n, n]
        