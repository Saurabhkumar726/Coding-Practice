class Solution:
    def maxSubarrayXOR(self, arr, k):
        x = 0
        for i in range(k):
            x ^= arr[i]
        
        ans = x
        
        for i in range(k, len(arr)):
            x ^= arr[i - k]
            x ^= arr[i]
            ans = max(ans, x)
        
        return ans