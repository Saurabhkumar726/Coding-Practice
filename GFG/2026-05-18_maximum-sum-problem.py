class Solution:
    def maxSum(self, n):
        dp = {}
        
        def solve(x):
            if x == 0:
                return 0
            
            if x in dp:
                return dp[x]
            
            dp[x] = max(x, solve(x // 2) + solve(x // 3) + solve(x // 4))
            return dp[x]
        
        return solve(n)