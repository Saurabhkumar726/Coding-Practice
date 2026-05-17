from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [False] * n
        q = deque([start])
        vis[start] = True
        
        while q:
            i = q.popleft()
            
            if arr[i] == 0:
                return True
            
            for nxt in [i + arr[i], i - arr[i]]:
                if 0 <= nxt < n and not vis[nxt]:
                    vis[nxt] = True
                    q.append(nxt)
        
        return False