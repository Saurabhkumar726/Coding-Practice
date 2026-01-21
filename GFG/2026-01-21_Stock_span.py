class Solution:
    def calculateSpan(self, arr):
        stack = []      
        span = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            span[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)

        return span

        