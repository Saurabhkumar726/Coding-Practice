class Solution:
    def countSubset(self, arr, k):
        from collections import Counter

        n = len(arr)
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        def gen(nums):
            res = [0]
            for x in nums:
                res += [s + x for s in res]
            return res

        L = gen(left)
        R = gen(right)

        freq = Counter(R)
        ans = 0

        for s in L:
            ans += freq[k - s]

        return ans
