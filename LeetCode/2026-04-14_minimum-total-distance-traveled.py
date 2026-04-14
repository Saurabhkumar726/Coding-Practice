from typing import List
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        m = len(robot)
        n = len(factory)
        
        @lru_cache(None)
        def dp(i, j, used):
            if i == m:
                return 0
            if j == n:
                return float('inf')
            
            pos, limit = factory[j]
            
            res = dp(i, j + 1, 0)
            
            if used < limit:
                cost = abs(robot[i] - pos)
                res = min(res, cost + dp(i + 1, j, used + 1))
            
            return res
        
        return dp(0, 0, 0)