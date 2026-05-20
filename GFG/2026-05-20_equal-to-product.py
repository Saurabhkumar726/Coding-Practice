class Solution:
    def isProduct(self, arr, target):
        seen = set()
        
        for num in arr:
            if num == 0:
                if target == 0:
                    return True
            else:
                if target % num == 0 and (target // num) in seen:
                    return True
            
            seen.add(num)
        
        return False