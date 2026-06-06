class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        total_cells = n * m
        
        total_placements = total_cells * (total_cells - 1)
        
        attacking = 4 * ((n - 1) * (m - 2) + (n - 2) * (m - 1))
        
        return total_placements - attacking