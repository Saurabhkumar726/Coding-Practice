class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        
        result = [[1] * m for _ in range(n)]
        
        prefix = 1
        for i in range(n):
            for j in range(m):
                result[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                result[i][j] = (result[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD
        
        return result