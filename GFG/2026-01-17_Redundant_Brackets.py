class Solution():
    def checkRedundancy(self, s):
        stack = []

        for ch in s:
            if ch == ')':
                top = stack.pop()
                has_operator = False

                while top != '(':
                    if top in '+-*/':
                        has_operator = True
                    top = stack.pop()

                if not has_operator:
                    return True
            else:
                stack.append(ch)

        return False
