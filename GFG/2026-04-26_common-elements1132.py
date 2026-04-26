class Solution:
    def commonElements(self, a, b, c):
        i = j = k = 0
        n1, n2, n3 = len(a), len(b), len(c)
        res = []
        last = None
        
        while i < n1 and j < n2 and k < n3:
            if a[i] == b[j] == c[k]:
                if last != a[i]:
                    res.append(a[i])
                    last = a[i]
                i += 1
                j += 1
                k += 1
            else:
                mn = min(a[i], b[j], c[k])
                if a[i] == mn:
                    i += 1
                elif b[j] == mn:
                    j += 1
                else:
                    k += 1
        
        return res