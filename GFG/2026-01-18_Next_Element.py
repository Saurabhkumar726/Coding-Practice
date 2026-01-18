from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        n = len(arr)
        freq = Counter(arr)
        res = [-1] * n
        stack = []

        for i in range(n):
            while stack and freq[arr[i]] > freq[arr[stack[-1]]]:
                res[stack.pop()] = arr[i]
            stack.append(i)

        return res
