from collections import deque

class Solution:
    def minTime(self, root, target):
        parent = {}
        
        def build(node, par):
            if not node:
                return
            parent[node] = par
            build(node.left, node)
            build(node.right, node)
        
        build(root, None)
        
        start = None
        def find(node):
            nonlocal start
            if not node:
                return
            if node.data == target:
                start = node
                return
            find(node.left)
            find(node.right)
        
        find(root)
        
        q = deque([start])
        visited = set([start])
        time = -1
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                for nei in [node.left, node.right, parent[node]]:
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            time += 1
        
        return time