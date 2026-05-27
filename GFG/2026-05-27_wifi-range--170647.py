class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        covered = [0] * (n + 1)
        
        for i in range(n):
            if s[i] == '1':
                left = max(0, i - x)
                right = min(n - 1, i + x)
                
                covered[left] += 1
                covered[right + 1] -= 1
        
        curr = 0
        
        for i in range(n):
            curr += covered[i]
            
            if curr <= 0:
                return False
        
        return True