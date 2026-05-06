class Solution:
    def getSize(self, root):
        if not root:
            return 0
        
        return 1 + self.getSize(root.left) + self.getSize(root.right)