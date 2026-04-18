class Solution:
    def maxOnes(self, arr):
        total_ones = sum(arr)
        
        max_gain = 0
        curr = 0
        
        for x in arr:
            val = 1 if x == 0 else -1
            
            curr = max(val, curr + val)
            max_gain = max(max_gain, curr)
        
        return total_ones + max_gain