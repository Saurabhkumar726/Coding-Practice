from typing import List
from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dfs(i):
            ans = 1

            for step in range(1, d + 1):
                ni = i - step

                if ni < 0 or arr[ni] >= arr[i]:
                    break

                ans = max(ans, 1 + dfs(ni))

            for step in range(1, d + 1):
                ni = i + step

                if ni >= n or arr[ni] >= arr[i]:
                    break

                ans = max(ans, 1 + dfs(ni))

            return ans

        return max(dfs(i) for i in range(n))