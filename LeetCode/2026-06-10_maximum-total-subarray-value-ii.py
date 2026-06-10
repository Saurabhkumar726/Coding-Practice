from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []

        for i in range(n):
            mn = mx = nums[i]

            for j in range(i, n):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])

                val = mx - mn

                if len(heap) < k:
                    heapq.heappush(heap, val)
                elif val > heap[0]:
                    heapq.heapreplace(heap, val)

        return sum(heap)