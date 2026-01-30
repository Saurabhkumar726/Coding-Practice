class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2
        res = []
        for i in range(half):
            res.append(q[i])
            res.append(q[i + half])
        q.clear()
        for x in res:
            q.append(x)
