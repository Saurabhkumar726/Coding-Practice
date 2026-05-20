from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        common = 0
        ans = []
        
        for a, b in zip(A, B):
            if a in seen:
                common += 1
            seen.add(a)
            
            if b in seen:
                common += 1
            seen.add(b)
            
            ans.append(common)
        
        return ans