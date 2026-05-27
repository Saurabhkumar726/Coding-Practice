class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                c = ch.lower()
                if c not in first_upper:
                    first_upper[c] = i
        
        ans = 0
        
        for c in last_lower:
            if c in first_upper and last_lower[c] < first_upper[c]:
                ans += 1
        
        return ans
        