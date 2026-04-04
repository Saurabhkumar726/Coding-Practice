class Solution:
    def graycode(self, n):
        res = [0]
        
        for i in range(n):
            for j in reversed(res):
                res.append(j | (1 << i))
        
        return [format(x, '0{}b'.format(n)) for x in res]