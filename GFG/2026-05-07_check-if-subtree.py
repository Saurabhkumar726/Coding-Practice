class Solution:
    def isSubTree(self, root1, root2):
        
        def identical(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (a.data == b.data and
                    identical(a.left, b.left) and
                    identical(a.right, b.right))
        
        if not root2:
            return True
        
        if not root1:
            return False
        
        if identical(root1, root2):
            return True
        
        return (self.isSubTree(root1.left, root2) or
                self.isSubTree(root1.right, root2))