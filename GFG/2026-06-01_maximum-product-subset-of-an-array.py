class Solution:
    def findMaxProduct(self, arr):
        mod = 1000000007
        
        if len(arr) == 1:
            return arr[0]
        
        neg_count = 0
        zero_count = 0
        max_neg = -11
        prod = 1
        
        for x in arr:
            if x == 0:
                zero_count += 1
                continue
            
            if x < 0:
                neg_count += 1
                max_neg = max(max_neg, x)
            
            prod *= x
        
        if zero_count == len(arr):
            return 0
        
        if neg_count == 1 and zero_count + neg_count == len(arr):
            return 0
        
        if neg_count % 2 == 1:
            prod //= max_neg
        
        return prod % mod