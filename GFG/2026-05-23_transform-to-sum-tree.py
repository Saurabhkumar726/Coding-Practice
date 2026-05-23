class Solution:
    def toSumTree(self, root):
        def solve(node):
            if not node:
                return 0
            
            old = node.data
            
            left = solve(node.left)
            right = solve(node.right)
            
            node.data = left + right
            
            return old + node.data
        
        solve(root)