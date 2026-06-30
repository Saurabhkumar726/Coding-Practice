class Solution:
    def minInsAndDel(self, a, b):
        pos = {}
        for i, val in enumerate(b):
            pos[val] = i

        arr = []
        for x in a:
            if x in pos:
                arr.append(pos[x])

        lis = []

        for x in arr:
            l, r = 0, len(lis)
            while l < r:
                mid = (l + r) // 2
                if lis[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            if l == len(lis):
                lis.append(x)
            else:
                lis[l] = x

        lcs = len(lis)
        return (len(a) - lcs) + (len(b) - lcs)