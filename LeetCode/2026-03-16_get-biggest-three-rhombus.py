from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()

        for i in range(m):
            for j in range(n):
                res.add(grid[i][j])
                d = 1
                while i-d >= 0 and i+d < m and j-d >= 0 and j+d < n:
                    total = 0

                    x, y = i-d, j
                    for k in range(d):
                        total += grid[x+k][y+k]

                    x, y = i, j+d
                    for k in range(d):
                        total += grid[x+k][y-k]

                    x, y = i+d, j
                    for k in range(d):
                        total += grid[x-k][y-k]

                    x, y = i, j-d
                    for k in range(d):
                        total += grid[x-k][y+k]

                    res.add(total)
                    d += 1

        return sorted(res, reverse=True)[:3]