class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        count = 0
        length = 1
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                length += 1
            else:
                if length >= 2:
                    count += (length * (length - 1)) // 2
                length = 1
        
        if length >= 2:
            count += (length * (length - 1)) // 2
        
        return count
