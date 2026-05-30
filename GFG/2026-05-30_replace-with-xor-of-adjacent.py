class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        res = [0] * n
        
        res[0] = arr[0] ^ arr[1]
        res[n - 1] = arr[n - 2] ^ arr[n - 1]
        
        for i in range(1, n - 1):
            res[i] = arr[i - 1] ^ arr[i + 1]
        
        for i in range(n):
            arr[i] = res[i]
        
        return arr