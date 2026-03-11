class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        stack = []
        left = [0]*n
        right = [0]*n

        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            left[i] = count

        stack = []

        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            right[i] = count

        ans = 0
        for i in range(n):
            ans += arr[i] * left[i] * right[i]

        return ans