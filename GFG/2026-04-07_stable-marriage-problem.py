from collections import deque

class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        
        rank = [[0]*n for _ in range(n)]
        for w in range(n):
            for i, m in enumerate(women[w]):
                rank[w][m] = i
        
        free = deque(range(n))
        next_prop = [0]*n
        partner_w = [-1]*n
        partner_m = [-1]*n
        
        while free:
            m = free.popleft()
            w = men[m][next_prop[m]]
            next_prop[m] += 1
            
            if partner_w[w] == -1:
                partner_w[w] = m
                partner_m[m] = w
            else:
                m2 = partner_w[w]
                if rank[w][m] < rank[w][m2]:
                    partner_w[w] = m
                    partner_m[m] = w
                    partner_m[m2] = -1
                    free.append(m2)
                else:
                    free.append(m)
        
        return partner_m