class Solution:
    def subarrayXor(self, arr, k):
        freq = {0: 1}
        prefix_xor = 0
        count = 0
        
        for num in arr:
            prefix_xor ^= num
            
            if (prefix_xor ^ k) in freq:
                count += freq[prefix_xor ^ k]
            
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count