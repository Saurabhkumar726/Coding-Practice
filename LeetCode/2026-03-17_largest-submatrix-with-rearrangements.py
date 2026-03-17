from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0]*n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1
            
            temp = sorted(heights, reverse=True)
            
            for j in range(n):
                ans = max(ans, temp[j] * (j+1))
        
        return ans