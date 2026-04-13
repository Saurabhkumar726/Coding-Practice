class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        res = num[:]
        
        i, j = 0, n - 1
        while i < j:
            res[j] = res[i]
            i += 1
            j -= 1
        
        if res > num:
            return res
        
        carry = 1
        mid = n // 2
        
        if n % 2 == 1:
            res[mid] += 1
            carry = res[mid] // 10
            res[mid] %= 10
            i = mid - 1
            j = mid + 1
        else:
            i = mid - 1
            j = mid
        
        while i >= 0 and carry:
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10
            res[j] = res[i]
            i -= 1
            j += 1
        
        if carry:
            res = [1] + [0] * (n - 1) + [1]
        
        return res
        