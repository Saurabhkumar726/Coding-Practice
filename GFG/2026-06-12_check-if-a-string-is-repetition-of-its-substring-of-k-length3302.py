class Solution:
    def kSubstr(self, s, k):
        n = len(s)

        if n % k != 0:
            return False

        blocks = [s[i:i + k] for i in range(0, n, k)]

        freq = {}
        for block in blocks:
            freq[block] = freq.get(block, 0) + 1

        if len(freq) == 1:
            return True

        if len(freq) == 2:
            return min(freq.values()) == 1

        if len(blocks) == 2:
            return True

        return False
        