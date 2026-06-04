class Solution:
    def maxSubstring(self, s):
        curr = 0
        best = 0
        
        for ch in s:
            val = 1 if ch == '0' else -1
            
            curr = max(val, curr + val)
            best = max(best, curr)
        
        return -1 if best == 0 else best
		