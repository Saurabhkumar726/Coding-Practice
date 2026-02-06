class Solution:
    def smallestDiff(self, a, b, c):
        a.sort()
        b.sort()
        c.sort()
        
        i = j = k = 0
        best_diff = float('inf')
        best_sum = float('inf')
        best_triplet = []
        
        while i < len(a) and j < len(b) and k < len(c):
            x, y, z = a[i], b[j], c[k]
            mx = max(x, y, z)
            mn = min(x, y, z)
            diff = mx - mn
            s = x + y + z
            
            if diff < best_diff or (diff == best_diff and s < best_sum):
                best_diff = diff
                best_sum = s
                best_triplet = [x, y, z]
            
            if mn == x:
                i += 1
            elif mn == y:
                j += 1
            else:
                k += 1
        
        best_triplet.sort(reverse=True)
        return best_triplet
