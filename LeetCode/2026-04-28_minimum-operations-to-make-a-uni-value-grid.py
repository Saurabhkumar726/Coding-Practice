from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        base = grid[0][0]
        
        for row in grid:
            for val in row:
                if (val - base) % x != 0:
                    return -1
                arr.append(val)
        
        arr.sort()
        median = arr[len(arr) // 2]
        
        ops = 0
        for val in arr:
            ops += abs(val - median) // x
        
        return ops