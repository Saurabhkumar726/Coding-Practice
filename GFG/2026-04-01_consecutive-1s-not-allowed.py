class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2
        
        a, b = 1, 1
        
        for _ in range(2, n + 1):
            a, b = a + b, a
        
        return a + b