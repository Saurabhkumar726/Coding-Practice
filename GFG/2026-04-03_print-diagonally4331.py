class Solution:
    def diagView(self, mat):
        n = len(mat)
        res = []
        
        for d in range(2 * n - 1):
            i = 0 if d < n else d - n + 1
            j = d if d < n else n - 1
            
            while i < n and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
        
        return res