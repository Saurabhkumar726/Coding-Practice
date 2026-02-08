class Solution:
    def maxProduct(self, arr):
        max_ending = arr[0]
        min_ending = arr[0]
        result = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] < 0:
                max_ending, min_ending = min_ending, max_ending
            
            max_ending = max(arr[i], max_ending * arr[i])
            min_ending = min(arr[i], min_ending * arr[i])
            
            result = max(result, max_ending)
        
        return result