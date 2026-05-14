class Solution:
    def search(self, a, b):
        n = len(a)
        m = len(b)
        
        lps = [0] * m
        j = 0
        
        for i in range(1, m):
            while j > 0 and b[i] != b[j]:
                j = lps[j - 1]
            
            if b[i] == b[j]:
                j += 1
                lps[i] = j
        
        ans = []
        j = 0
        
        for i in range(n):
            while j > 0 and a[i] != b[j]:
                j = lps[j - 1]
            
            if a[i] == b[j]:
                j += 1
            
            if j == m:
                ans.append(i - m + 1)
                j = lps[j - 1]
        
        return ans