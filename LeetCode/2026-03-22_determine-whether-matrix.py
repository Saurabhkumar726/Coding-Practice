class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate90(matrix):
            n = len(matrix)
            rotated = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated[j][n - 1 - i] = matrix[i][j]
            return rotated
        
        current = mat
        for _ in range(4):
            if current == target:
                return True
            current = rotate90(current)
        
        return False