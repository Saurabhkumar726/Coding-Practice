class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        total_sum = sum(sum(row) for row in grid)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # Check horizontal cuts
        current_sum = 0
        for i in range(m - 1):
            current_sum += sum(grid[i])
            if current_sum == target:
                return True
        
        # Check vertical cuts
        current_sum = 0
        for j in range(n - 1):
            col_sum = sum(grid[i][j] for i in range(m))
            current_sum += col_sum
            if current_sum == target:
                return True
        
        return False