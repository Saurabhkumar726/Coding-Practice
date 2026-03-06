class Solution:
    def minWindow(self, s, p):
        from collections import Counter
        
        need = Counter(p)
        window = {}
        have = 0
        need_count = len(need)
        left = 0
        res = ""
        res_len = float("inf")
        
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == need_count:
                if right - left + 1 < res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        
        return res