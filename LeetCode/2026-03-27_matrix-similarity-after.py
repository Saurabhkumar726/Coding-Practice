class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        
        k = k % n
        
        # If k is 0 after modulo, matrix remains the same
        if k == 0:
            return True
        
        for i in range(m):
            if i % 2 == 0:

                shifted = mat[i][k:] + mat[i][:k]
            else:

                shifted = mat[i][-k:] + mat[i][:-k]
            
            if shifted != mat[i]:
                return False
        
        return True