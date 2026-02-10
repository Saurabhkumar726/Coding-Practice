class Solution:
    def kokoEat(self, arr, k):
        import math
        
        left, right = 1, max(arr)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            
            for pile in arr:
                hours += math.ceil(pile / mid)
            
            if hours <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
