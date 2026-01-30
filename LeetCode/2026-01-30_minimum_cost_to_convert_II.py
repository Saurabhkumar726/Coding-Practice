from typing import List
import math

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        strs = set(original) | set(changed)
        idx = {s:i for i,s in enumerate(strs)}
        m = len(strs)
        dist = [[math.inf]*m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
        for o,c,w in zip(original,changed,cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)

        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        n = len(source)
        dp = [math.inf]*(n+1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == math.inf:
                continue
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            for s in strs:
                L = len(s)
                if i+L <= n and source[i:i+L] == s:
                    t = target[i:i+L]
                    if t in idx:
                        d = dist[idx[s]][idx[t]]
                        if d < math.inf:
                            dp[i+L] = min(dp[i+L], dp[i] + d)

        return -1 if dp[n] == math.inf else dp[n]
