class Solution:
    def minToggle(self, arr):
        n = len(arr)
        
        prefix1 = [0] * (n + 1)
        suffix0 = [0] * (n + 1)
        
        for i in range(n):
            prefix1[i + 1] = prefix1[i] + (1 if arr[i] == 1 else 0)
        
        for i in range(n - 1, -1, -1):
            suffix0[i] = suffix0[i + 1] + (1 if arr[i] == 0 else 0)
        
        ans = n
        
        for i in range(n + 1):
            ans = min(ans, prefix1[i] + suffix0[i])
        
        return ans