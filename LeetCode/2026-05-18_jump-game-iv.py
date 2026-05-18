from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n == 1:
            return 0
        
        mp = defaultdict(list)
        
        for i, val in enumerate(arr):
            mp[val].append(i)
        
        q = deque([(0, 0)])
        vis = [False] * n
        vis[0] = True
        
        while q:
            i, steps = q.popleft()
            
            if i == n - 1:
                return steps
            
            neighbors = mp[arr[i]] + [i - 1, i + 1]
            
            for nxt in neighbors:
                if 0 <= nxt < n and not vis[nxt]:
                    vis[nxt] = True
                    q.append((nxt, steps + 1))
            
            mp[arr[i]].clear()
        
        return -1