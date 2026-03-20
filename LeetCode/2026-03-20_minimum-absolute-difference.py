from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = []
        
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = set()
                
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.add(grid[x][y])
                
                arr = sorted(vals)
                
                if len(arr) <= 1:
                    row.append(0)
                else:
                    min_diff = float('inf')
                    for t in range(len(arr) - 1):
                        min_diff = min(min_diff, arr[t+1] - arr[t])
                    row.append(min_diff)
            
            res.append(row)
        
        return res