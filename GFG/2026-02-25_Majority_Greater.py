class Solution:
    def longestSubarray(self, arr, k):
        prefix = 0
        first_occurrence = {}
        max_len = 0
        
        for i in range(len(arr)):
            if arr[i] > k:
                prefix += 1
            else:
                prefix -= 1
            
            if prefix > 0:
                max_len = i + 1
            else:
                if prefix - 1 in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[prefix - 1])
            
            if prefix not in first_occurrence:
                first_occurrence[prefix] = i
        
        return max_len