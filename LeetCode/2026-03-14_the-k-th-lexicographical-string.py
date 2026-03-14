class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        
        def dfs(s):
            if len(s) == n:
                res.append(s)
                return
            for c in "abc":
                if not s or s[-1] != c:
                    dfs(s + c)
        
        dfs("")
        
        if k > len(res):
            return ""
        return res[k-1]