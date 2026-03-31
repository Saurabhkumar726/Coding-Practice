class Solution:
    def maxProfit(self, arr, k):
        n = len(arr)
        if n == 0:
            return 0

        hold = -arr[0]
        sold = 0
        
        for i in range(1, n):

            new_hold = max(hold, sold - arr[i])
            
            new_sold = max(sold, hold + arr[i] - k)
            
            hold = new_hold
            sold = new_sold
        
        return sold