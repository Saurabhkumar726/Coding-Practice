from collections import Counter

class Solution:
    def canFormPalindrome(self, s):
        freq = Counter(s)
        odd = 0
        
        for v in freq.values():
            if v % 2 != 0:
                odd += 1
        
        return odd <= 1