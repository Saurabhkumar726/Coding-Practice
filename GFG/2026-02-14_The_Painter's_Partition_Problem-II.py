class Solution:
    def minTime(self, arr, k):
        left = max(arr)
        right = sum(arr)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            painters = 1
            current_sum = 0
            
            for length in arr:
                if current_sum + length <= mid:
                    current_sum += length
                else:
                    painters += 1
                    current_sum = length
            
            if painters <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
