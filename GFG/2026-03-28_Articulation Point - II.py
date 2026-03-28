from collections import defaultdict

class Solution:
    def articulationPoints(self, V, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * V
        disc = [0] * V
        low = [0] * V
        parent = [-1] * V
        ap = [False] * V
        self.time = 0
        
        def dfs(u):
            children = 0
            visited[u] = True
            disc[u] = low[u] = self.time
            self.time += 1
            
            for v in graph[u]:
                if not visited[v]:
                    children += 1
                    parent[v] = u
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    # Check if u is an articulation point
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        result = [i for i in range(V) if ap[i]]
        
        return result if result else [-1]