from typing import List
import math

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7

        def modpow(a, e):
            r = 1
            while e:
                if e & 1:
                    r = r * a % MOD
                a = a * a % MOD
                e >>= 1
            return r

        n = len(nums)
        B = int(math.sqrt(n)) + 1

        events = [[] for _ in range(B + 1)]
        for k in range(1, B + 1):
            events[k] = [[] for _ in range(k)]

        for l, r, k, v in queries:
            if k > B:
                i = l
                while i <= r:
                    nums[i] = nums[i] * v % MOD
                    i += k
            else:
                rem = l % k
                start = (l - rem) // k
                end = (r - rem) // k

                events[k][rem].append((start, v))

                maxT = (n - 1 - rem) // k
                if end + 1 <= maxT:
                    inv = modpow(v, MOD - 2)
                    events[k][rem].append((end + 1, inv))

        for k in range(1, B + 1):
            for rem in range(k):
                ev = events[k][rem]
                if not ev:
                    continue

                ev.sort()

                comp = []
                for p in ev:
                    if comp and comp[-1][0] == p[0]:
                        comp[-1] = (comp[-1][0], comp[-1][1] * p[1] % MOD)
                    else:
                        comp.append(p)

                cur = 1
                ptr = 0
                t = 0
                idx = rem

                while idx < n:
                    while ptr < len(comp) and comp[ptr][0] == t:
                        cur = cur * comp[ptr][1] % MOD
                        ptr += 1

                    nums[idx] = nums[idx] * cur % MOD
                    idx += k
                    t += 1

        ans = 0
        for x in nums:
            ans ^= x

        return ans