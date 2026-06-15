class Solution:
    def minimumCost(self, cost, w):
        INF = float('inf')
        dp = [INF] * (w + 1)
        dp[0] = 0

        for i in range(len(cost)):
            if cost[i] == -1:
                continue

            weight = i + 1
            price = cost[i]

            for j in range(weight, w + 1):
                dp[j] = min(dp[j], dp[j - weight] + price)

        return -1 if dp[w] == INF else dp[w]
        