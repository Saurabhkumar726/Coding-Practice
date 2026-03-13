from typing import List
import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can(t):
            total = 0
            for w in workerTimes:
                x = int((math.sqrt(1 + 8 * t / w) - 1) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False

        l, r = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = r

        while l <= r:
            m = (l + r) // 2
            if can(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans