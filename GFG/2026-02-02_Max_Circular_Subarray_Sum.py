class Solution:
    def maxCircularSum(self, arr):
        total = 0
        max_sum = arr[0]
        cur_max = 0
        min_sum = arr[0]
        cur_min = 0

        for x in arr:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)

            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)

            total += x

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)

        