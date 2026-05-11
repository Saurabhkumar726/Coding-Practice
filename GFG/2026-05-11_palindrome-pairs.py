class Solution:
    def palindromePair(self, arr):
        mp = {}
        
        for word in arr:
            mp[word] = mp.get(word, 0) + 1
        
        def isPal(s):
            return s == s[::-1]
        
        for word in arr:
            n = len(word)
            
            for i in range(n + 1):
                left = word[:i]
                right = word[i:]
                
                if isPal(left):
                    rev = right[::-1]
                    if rev in mp and (rev != word or mp[rev] > 1):
                        return True
                
                if i != n and isPal(right):
                    rev = left[::-1]
                    if rev in mp and (rev != word or mp[rev] > 1):
                        return True
        
        return False