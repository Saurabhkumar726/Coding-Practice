class Solution:
    def sumDiffPairs(self, arr, k):
        arr.sort()
        n = len(arr)
        
        dp = [0] * n
        
        for i in range(1, n):
            dp[i] = dp[i - 1]
            
            if arr[i] - arr[i - 1] < k:
                pair_sum = arr[i] + arr[i - 1]
                
                if i >= 2:
                    pair_sum += dp[i - 2]
                
                dp[i] = max(dp[i], pair_sum)
        
        return dp[n - 1]