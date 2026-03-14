from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        q = deque([(root, 0)])
        m = {}
        
        while q:
            node, hd = q.popleft()
            
            if hd not in m:
                m[hd] = node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        return [m[x] for x in sorted(m)]