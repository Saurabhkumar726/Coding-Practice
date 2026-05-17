class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        stack = []
        
        for num in arr:
            if stack and ((stack[-1] >= 0 and num < 0) or (stack[-1] < 0 and num >= 0)):
                stack.pop()
            else:
                stack.append(num)
        
        return stack