class Solution:
    def sortBySetBitCount(self, arr):
        return sorted(arr, key=lambda x: (-bin(x).count('1')))