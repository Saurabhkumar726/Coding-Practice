from collections import deque, defaultdict

class Solution:
    def minHeightRoot(self, V, edges):
        if V == 1:
            return [0]
        
        graph = defaultdict(list)
        degree = [0] * V
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        queue = deque()
        for i in range(V):
            if degree[i] == 1:
                queue.append(i)
        
        remaining = V
        
        while remaining > 2:
            size = len(queue)
            remaining -= size
            
            for _ in range(size):
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        
        return sorted(list(queue))