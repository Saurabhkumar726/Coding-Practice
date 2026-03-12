class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        hint = [0]*n
        flip = 0
        ans = 0
        
        for i in range(n):
            if i >= k:
                flip ^= hint[i-k]
            
            if arr[i] ^ flip == 0:
                if i + k > n:
                    return -1
                ans += 1
                flip ^= 1
                hint[i] = 1
        
        return ans
        