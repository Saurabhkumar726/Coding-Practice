class Solution:
    def countWays(self, n, k):
        if n == 1:
            return k
        same = k
        diff = k * (k - 1)
        
        for _ in range(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1)
        
        return same + diff