from typing import List
from bisect import bisect_right

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def build(start, duration):
            rides = sorted(zip(start, duration))
            s = [x for x, _ in rides]
            d = [y for _, y in rides]
            n = len(rides)

            pref = [0] * n
            pref[0] = d[0]
            for i in range(1, n):
                pref[i] = min(pref[i - 1], d[i])

            suff = [0] * n
            suff[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suff[i] = min(suff[i + 1], s[i] + d[i])

            return s, pref, suff

        waterS, waterPref, waterSuff = build(waterStartTime, waterDuration)
        landS, landPref, landSuff = build(landStartTime, landDuration)

        INF = float('inf')
        ans = INF

        for ls, ld in zip(landStartTime, landDuration):
            t = ls + ld
            idx = bisect_right(waterS, t)

            best = INF
            if idx > 0:
                best = min(best, t + waterPref[idx - 1])
            if idx < len(waterS):
                best = min(best, waterSuff[idx])

            ans = min(ans, best)

        for ws, wd in zip(waterStartTime, waterDuration):
            t = ws + wd
            idx = bisect_right(landS, t)

            best = INF
            if idx > 0:
                best = min(best, t + landPref[idx - 1])
            if idx < len(landS):
                best = min(best, landSuff[idx])

            ans = min(ans, best)

        return ans
        