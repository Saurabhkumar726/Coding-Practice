class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        ans = 0
        
        for bit in range(32):
            count1 = 0
            for num in arr:
                if (num >> bit) & 1:
                    count1 += 1
            count0 = n - count1
            ans += (count1 * count0) * (1 << bit)
        
        return ans