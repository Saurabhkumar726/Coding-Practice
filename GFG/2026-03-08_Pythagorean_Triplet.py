class Solution:
    def pythagoreanTriplet(self, arr):
        sq = set(x*x for x in arr)
        n = len(arr)
        
        for i in range(n):
            for j in range(i+1, n):
                if arr[i]*arr[i] + arr[j]*arr[j] in sq:
                    return True
        
        return False