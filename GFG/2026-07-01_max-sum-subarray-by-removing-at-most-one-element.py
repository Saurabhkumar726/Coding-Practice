class Solution:
    def maxSumSubarray(self, arr):
        n = len(arr)

        no_skip = arr[0]
        one_skip = float('-inf')
        ans = arr[0]

        for i in range(1, n):
            one_skip = max(one_skip + arr[i], no_skip)
            no_skip = max(no_skip + arr[i], arr[i])
            ans = max(ans, no_skip, one_skip)

        return ans
        