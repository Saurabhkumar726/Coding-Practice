class Solution:
    def longestCycle(self, V, edges):
        graph = [-1] * V
        for u, v in edges:
            graph[u] = v
        
        visited = [False] * V
        max_cycle_length = -1
        
        for start in range(V):
            if visited[start]:
                continue
            
            distance = {}
            current = start
            dist = 0
            
            while current != -1 and current not in distance and not visited[current]:
                distance[current] = dist
                dist += 1
                current = graph[current]
            
            if current != -1 and current in distance:
                cycle_length = dist - distance[current]
                max_cycle_length = max(max_cycle_length, cycle_length)
            
            for node in distance:
                visited[node] = True
        
        return max_cycle_length