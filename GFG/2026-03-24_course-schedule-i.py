from collections import deque, defaultdict

class Solution:
    def canFinish(self, n, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * n
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        completed = 0
        
        while queue:
            node = queue.popleft()
            completed += 1
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return completed == n