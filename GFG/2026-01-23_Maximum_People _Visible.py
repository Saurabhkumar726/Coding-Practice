class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        left_block = [-1] * n
        right_block = [n] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left_block[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            right_block[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            seen = (i - left_block[i] - 1) + (right_block[i] - i - 1) + 1
            ans = max(ans, seen)

        return ans
