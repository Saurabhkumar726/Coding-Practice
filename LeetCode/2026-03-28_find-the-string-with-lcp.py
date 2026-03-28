from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        res = [''] * n
        ch = ord('a')
        
        for i in range(n):
            if res[i]:
                continue
            if ch > ord('z'):
                return ""
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = chr(ch)
            ch += 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i] == res[j]:
                    expected = 1
                    if i + 1 < n and j + 1 < n:
                        expected += lcp[i + 1][j + 1]
                else:
                    expected = 0
                if lcp[i][j] != expected:
                    return ""
        
        return "".join(res)