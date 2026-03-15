from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root): 
        if not root:
            return []
        
        m = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            m[hd].append(node.data)
            
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        res = []
        for k in sorted(m):
            res.append(m[k])
        
        return res