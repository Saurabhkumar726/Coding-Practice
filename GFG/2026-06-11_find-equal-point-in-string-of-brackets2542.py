class Solution:
    def findIndex(self, s):
        n = len(s)
        
        right_close = s.count(')')
        left_open = 0
        
        for i in range(n):
            if right_close == left_open:
                return i
            
            if s[i] == '(':
                left_open += 1
            else:
                right_close -= 1
        
        return n
