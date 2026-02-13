class Solution:
    def getCount(self, n, d):
        
        def digit_sum(x):
            return sum(int(c) for c in str(x))
        
        left, right = 1, n
        first_valid = n + 1
        
        while left <= right:
            mid = (left + right) // 2
            if mid - digit_sum(mid) >= d:
                first_valid = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if first_valid > n:
            return 0
        
        return n - first_valid + 1
