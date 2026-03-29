class Solution:
    def countPartitions(self, arr, diff):
        total_sum = sum(arr)
        n = len(arr)
        
        
        if (total_sum + diff) % 2 != 0 or total_sum < diff:
            return 0
        
        target = (total_sum + diff) // 2
        
        if target < 0:
            return 0
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]
        
