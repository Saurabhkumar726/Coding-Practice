class Solution:
    def findClosestPair(self, arr1, arr2, x):
        i = 0
        j = len(arr2) - 1
        diff = float('inf')
        res = (0, 0)
        
        while i < len(arr1) and j >= 0:
            s = arr1[i] + arr2[j]
            
            if abs(s - x) < diff:
                diff = abs(s - x)
                res = (arr1[i], arr2[j])
            
            if s > x:
                j -= 1
            else:
                i += 1
        
        return list(res)


        