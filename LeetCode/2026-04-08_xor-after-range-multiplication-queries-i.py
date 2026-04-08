from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        
        for l, r, k, v in queries:
            i = l
            while i <= r:
                nums[i] = (nums[i] * v) % mod
                i += k
        
        ans = 0
        for x in nums:
            ans ^= x
        
        return ans