class Solution:
    def largestBst(self, root):
        self.ans = 0
        
        def solve(node):
            if not node:
                return (float('inf'), float('-inf'), 0)
            
            left_min, left_max, left_size = solve(node.left)
            right_min, right_max, right_size = solve(node.right)
            
            if left_max < node.data < right_min:
                size = left_size + right_size + 1
                self.ans = max(self.ans, size)
                
                return (min(left_min, node.data), max(right_max, node.data), size)
            
            return (float('-inf'), float('inf'), 0)
        
        solve(root)
        return self.ans