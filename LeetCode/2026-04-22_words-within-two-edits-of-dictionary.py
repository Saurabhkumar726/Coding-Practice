from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def isValid(q, d):
            diff = 0
            for i in range(len(q)):
                if q[i] != d[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True
        
        res = []
        
        for q in queries:
            for d in dictionary:
                if isValid(q, d):
                    res.append(q)
                    break
        
        return res