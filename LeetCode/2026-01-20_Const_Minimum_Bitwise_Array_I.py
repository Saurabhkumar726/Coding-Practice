from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for x in nums:
            found = -1
            for a in range(x):
                if (a | (a + 1)) == x:
                    found = a
                    break
            res.append(found)

        return res
