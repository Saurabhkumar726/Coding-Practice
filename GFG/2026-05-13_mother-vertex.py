class Solution:
    def findMotherVertex(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
        
        def dfs(node, vis):
            vis[node] = True
            for nei in adj[node]:
                if not vis[nei]:
                    dfs(nei, vis)
        
        candidate = -1
        vis = [False] * V
        
        for i in range(V):
            if not vis[i]:
                dfs(i, vis)
                candidate = i
        
        vis = [False] * V
        dfs(candidate, vis)
        
        if not all(vis):
            return -1
        
        ans = candidate
        
        for i in range(candidate):
            vis = [False] * V
            dfs(i, vis)
            if all(vis):
                ans = i
                break
        
        return ans