class Solution:
    def maxChocolate(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]
        
        def solve(i, j1, j2):

            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')
            
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            
            if j1 == j2:
                chocolates = grid[i][j1]
            else:
                chocolates = grid[i][j1] + grid[i][j2]
            
            max_next = float('-inf')
            for dj1 in [-1, 0, 1]:
                for dj2 in [-1, 0, 1]:
                    max_next = max(max_next, solve(i + 1, j1 + dj1, j2 + dj2))
            
            dp[i][j1][j2] = chocolates + max_next
            return dp[i][j1][j2]
        
        return solve(0, 0, m - 1)