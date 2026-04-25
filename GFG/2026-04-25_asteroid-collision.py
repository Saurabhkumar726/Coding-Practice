class Solution:
    def reducePairs(self, arr):
        stack = []
        
        for x in arr:
            while stack and stack[-1] * x < 0:
                if abs(stack[-1]) > abs(x):
                    x = None
                    break
                elif abs(stack[-1]) < abs(x):
                    stack.pop()
                else:
                    stack.pop()
                    x = None
                    break
            
            if x is not None:
                stack.append(x)
        
        return stack