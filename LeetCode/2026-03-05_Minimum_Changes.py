class Solution:
    def minOperations(self, s: str) -> int:
        alt1 = 0
        alt2 = 0
        
        for i, c in enumerate(s):
            if c != "01"[i % 2]:
                alt1 += 1
            if c != "10"[i % 2]:
                alt2 += 1
        
        return min(alt1, alt2)