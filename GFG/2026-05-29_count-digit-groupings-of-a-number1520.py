class Solution:
    def validGroups(self, s):
        n = len(s)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + int(s[i])
        
        total = prefix[n]
        dp = [[-1] * (total + 1) for _ in range(n + 1)]
        
        def solve(idx, prev_sum):
            if idx == n:
                return 1
            
            if dp[idx][prev_sum] != -1:
                return dp[idx][prev_sum]
            
            ans = 0
            
            for j in range(idx, n):
                curr_sum = prefix[j + 1] - prefix[idx]
                
                if curr_sum >= prev_sum:
                    ans += solve(j + 1, curr_sum)
            
            dp[idx][prev_sum] = ans
            return ans
        
        return solve(0, 0)
        