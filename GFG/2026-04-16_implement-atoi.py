class Solution:
    def myAtoi(self, s):
        i, n = 0, len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            num = num * 10 + digit
            i += 1
        
        return sign * num
        