class Solution:
    def isPallindrome(self, N):
        b = bin(N)[2:]
        return 1 if b == b[::-1] else 0