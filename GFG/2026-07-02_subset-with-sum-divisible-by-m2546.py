class Solution:
    def divisibleByK(self, arr, k):
        dp = [False] * k
        dp[0] = False

        for num in arr:
            new_dp = dp[:]
            new_dp[num % k] = True

            for r in range(k):
                if dp[r]:
                    new_dp[(r + num) % k] = True

            dp = new_dp

            if dp[0]:
                return True

        return False