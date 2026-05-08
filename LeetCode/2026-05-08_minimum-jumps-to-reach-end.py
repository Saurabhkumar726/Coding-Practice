from typing import List
from collections import deque, defaultdict

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        def isPrime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True
        
        mp = defaultdict(list)
        
        for i, val in enumerate(nums):
            for p in set(self.factors(val)):
                mp[p].append(i)
        
        q = deque([(0, 0)])
        vis = [False] * n
        vis[0] = True
        used = set()
        
        while q:
            i, steps = q.popleft()
            
            if i == n - 1:
                return steps
            
            if i - 1 >= 0 and not vis[i - 1]:
                vis[i - 1] = True
                q.append((i - 1, steps + 1))
            
            if i + 1 < n and not vis[i + 1]:
                vis[i + 1] = True
                q.append((i + 1, steps + 1))
            
            val = nums[i]
            
            if isPrime(val) and val not in used:
                for nxt in mp[val]:
                    if not vis[nxt]:
                        vis[nxt] = True
                        q.append((nxt, steps + 1))
                used.add(val)
        
        return -1
    
    def factors(self, x):
        res = []
        d = 2
        
        while d * d <= x:
            while x % d == 0:
                res.append(d)
                x //= d
            d += 1
        
        if x > 1:
            res.append(x)
        
        return res