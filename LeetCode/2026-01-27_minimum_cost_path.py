import heapq
from typing import List
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))  
            graph[v].append((u, 2 * w))

        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in graph[u]:
                nc = cost + w
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(pq, (nc, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]
