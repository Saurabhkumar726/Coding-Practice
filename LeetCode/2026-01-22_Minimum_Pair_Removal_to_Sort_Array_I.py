from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0

        def is_non_decreasing(arr):
            return all(arr[i] >= arr[i-1] for i in range(1, len(arr)))

        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            nums[idx:idx + 2] = [min_sum]
            ops += 1

        return ops
