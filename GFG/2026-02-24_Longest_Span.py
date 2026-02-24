class Solution:
    def equalSumSpan(self, a1, a2):
        diff_map = {}
        max_len = 0
        prefix_diff = 0
        
        for i in range(len(a1)):
            prefix_diff += a1[i] - a2[i]
            
            if prefix_diff == 0:
                max_len = i + 1
            elif prefix_diff in diff_map:
                max_len = max(max_len, i - diff_map[prefix_diff])
            else:
                diff_map[prefix_diff] = i
        
        return max_len