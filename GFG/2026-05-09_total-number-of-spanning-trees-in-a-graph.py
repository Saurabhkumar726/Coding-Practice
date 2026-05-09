class Solution:
    def countSpanTree(self, n, edges):
        if n == 1:
            return 1
        
        lap = [[0] * n for _ in range(n)]
        
        for u, v in edges:
            lap[u][u] += 1
            lap[v][v] += 1
            lap[u][v] -= 1
            lap[v][u] -= 1
        
        mat = [row[1:] for row in lap[1:]]
        
        return round(self.det(mat))
    
    def det(self, mat):
        n = len(mat)
        res = 1
        
        for i in range(n):
            pivot = i
            
            while pivot < n and mat[pivot][i] == 0:
                pivot += 1
            
            if pivot == n:
                return 0
            
            if pivot != i:
                mat[i], mat[pivot] = mat[pivot], mat[i]
                res *= -1
            
            res *= mat[i][i]
            
            for j in range(i + 1, n):
                factor = mat[j][i] / mat[i][i]
                
                for k in range(i, n):
                    mat[j][k] -= factor * mat[i][k]
        
        return abs(res)