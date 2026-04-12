from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        
        def pos(c):
            idx = ord(c) - ord('A')
            return idx // 6, idx % 6
        
        def dist(a, b):
            if a == -1:
                return 0
            x1, y1 = pos(chr(a + ord('A')))
            x2, y2 = pos(chr(b + ord('A')))
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == n:
                return 0
            
            cur = ord(word[i]) - ord('A')
            
            use_f1 = dist(f1, cur) + dp(i + 1, cur, f2)
            use_f2 = dist(f2, cur) + dp(i + 1, f1, cur)
            
            return min(use_f1, use_f2)
        
        return dp(0, -1, -1)