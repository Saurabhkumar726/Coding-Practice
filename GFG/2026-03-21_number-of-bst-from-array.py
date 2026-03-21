class Solution:
    def countBSTs(self, arr):
        n = len(arr)
        result = []
        
        def catalan(n):
            if n <= 1:
                return 1
            dp = [0] * (n + 1)
            dp[0] = dp[1] = 1
            for i in range(2, n + 1):
                for j in range(i):
                    dp[i] += dp[j] * dp[i - 1 - j]
            return dp[n]
        
        for i in range(n):
            root = arr[i]
            left_count = sum(1 for x in arr if x < root)
            right_count = sum(1 for x in arr if x > root)
            result.append(catalan(left_count) * catalan(right_count))
        
        return result