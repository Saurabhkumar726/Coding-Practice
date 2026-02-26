class Solution:
    def areIsomorphic(self, s1: str, s2: str) -> bool:
        m1 = {}
        m2 = {}
        
        for c1, c2 in zip(s1, s2):
            if c1 in m1 and m1[c1] != c2:
                return False
            if c2 in m2 and m2[c2] != c1:
                return False
            m1[c1] = c2
            m2[c2] = c1
        
        return True