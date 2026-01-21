from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for x in nums:
            if x % 2 == 0:
                res.append(-1)
            else:
                # count trailing zeros of (x + 1)
                y = x + 1
                ctz = 0
                while (y & 1) == 0:
                    ctz += 1
                    y >>= 1

                k = ctz - 1
                res.append(x - (1 << k))

        return res
