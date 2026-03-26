import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7
        
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        dist = [float('inf')] * V
        ways = [0] * V
        
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, time in graph[u]:
                new_dist = dist[u] + time
                
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_dist, v))
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[V - 1]