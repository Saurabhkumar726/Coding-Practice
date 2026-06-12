from typing import List
from collections import deque
import math

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = math.ceil(math.log2(n)) + 1
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    up[nei][0] = node
                    q.append(nei)

        for j in range(1, LOG):
            for i in range(1, n + 1):
                if up[i][j - 1]:
                    up[i][j] = up[up[i][j - 1]][j - 1]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        ans = []

        for u, v in queries:
            ancestor = lca(u, v)
            edges_count = depth[u] + depth[v] - 2 * depth[ancestor]

            if edges_count == 0:
                ans.append(0)
            else:
                ans.append(pow(2, edges_count - 1, MOD))

        return ans
        