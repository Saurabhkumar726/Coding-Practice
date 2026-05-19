from collections import deque

class Solution:
    def minSteps(self, arr, start, end):
        mod = 1000
        
        vis = [False] * mod
        q = deque([(start, 0)])
        vis[start] = True
        
        while q:
            num, steps = q.popleft()
            
            if num == end:
                return steps
            
            for x in arr:
                nxt = (num * x) % mod
                
                if not vis[nxt]:
                    vis[nxt] = True
                    q.append((nxt, steps + 1))
        
        return -1
