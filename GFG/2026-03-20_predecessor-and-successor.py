class Solution:
    def findPreSuc(self, root, key):
        pre = None
        suc = None
        
        curr = root
        
        while curr:
            if curr.data < key:
                pre = curr
                curr = curr.right
            elif curr.data > key:
                suc = curr
                curr = curr.left
            else:
                temp = curr.left
                while temp:
                    pre = temp
                    temp = temp.right
                
                temp = curr.right
                while temp:
                    suc = temp
                    temp = temp.left
                
                break
        
        return [pre, suc]