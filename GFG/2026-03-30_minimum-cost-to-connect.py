import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])
                edges.append((dist, i, j))
        
        edges.sort()
        
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        total_cost = 0
        edges_used = 0
        
        for dist, u, v in edges:
            if union(u, v):
                total_cost += dist
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return total_cost