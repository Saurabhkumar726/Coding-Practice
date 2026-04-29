class Solution:
    def minSwaps(self, arr):
        ones = sum(arr)
        
        if ones == 0:
            return -1
        
        curr = sum(arr[:ones])
        max_ones = curr
        
        for i in range(ones, len(arr)):
            curr += arr[i] - arr[i - ones]
            max_ones = max(max_ones, curr)
        
        return ones - max_ones