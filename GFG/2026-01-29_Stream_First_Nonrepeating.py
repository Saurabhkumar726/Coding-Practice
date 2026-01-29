from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = [0]*26
        q = deque()
        res = []

        for ch in s:
            idx = ord(ch) - 97
            freq[idx] += 1
            q.append(ch)

            while q and freq[ord(q[0]) - 97] > 1:
                q.popleft()

            if q:
                res.append(q[0])
            else:
                res.append('#')

        return "".join(res)
