from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        pref = [[0]*m for _ in range(n)]
        countX = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                pref[i][j] = val
                countX[i][j] = 1 if grid[i][j] == 'X' else 0
                
                if i > 0:
                    pref[i][j] += pref[i-1][j]
                    countX[i][j] += countX[i-1][j]
                if j > 0:
                    pref[i][j] += pref[i][j-1]
                    countX[i][j] += countX[i][j-1]
                if i > 0 and j > 0:
                    pref[i][j] -= pref[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
        
        ans = 0
        
        for i in range(n):
            for j in range(m):
                total = pref[i][j]
                x_count = countX[i][j]
                
                if total == 0 and x_count > 0:
                    ans += 1
        
        return ans