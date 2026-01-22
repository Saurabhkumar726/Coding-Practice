class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        def sumSubarrayMins(nums):
            stack = []
            res = 0
            for i in range(n + 1):
                while stack and (i == n or nums[stack[-1]] > nums[i]):
                    mid = stack.pop()
                    left = stack[-1] if stack else -1
                    res += nums[mid] * (mid - left) * (i - mid)
                stack.append(i)
            return res

        def sumSubarrayMaxs(nums):
            stack = []
            res = 0
            for i in range(n + 1):
                while stack and (i == n or nums[stack[-1]] < nums[i]):
                    mid = stack.pop()
                    left = stack[-1] if stack else -1
                    res += nums[mid] * (mid - left) * (i - mid)
                stack.append(i)
            return res

        return sumSubarrayMaxs(arr) - sumSubarrayMins(arr)
