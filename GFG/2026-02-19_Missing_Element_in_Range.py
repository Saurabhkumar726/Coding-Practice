class Solution:
    def missingRange(self, arr, low, high):
        s = set(arr)
        res = []
        for num in range(low, high + 1):
            if num not in s:
                res.append(num)
        return res
