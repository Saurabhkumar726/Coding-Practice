from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        prev = list(range(-1, n - 1))
        next = list(range(1, n + 1))
        alive = [True] * n

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        def is_bad(i):
            j = next[i]
            return j < n and nums[i] > nums[j]

        bad = sum(is_bad(i) for i in range(n - 1))
        ops = 0

        while bad > 0:
            s, i = heapq.heappop(heap)
            j = next[i]
            if j >= n or not alive[i] or not alive[j]:
                continue
            if nums[i] + nums[j] != s:
                continue

            li, rj = prev[i], next[j]

            if li != -1:
                bad -= is_bad(li)
            bad -= is_bad(i)
            if rj < n:
                bad -= is_bad(j)

            nums[i] += nums[j]
            alive[j] = False
            next[i] = rj
            if rj < n:
                prev[rj] = i

            if li != -1:
                bad += is_bad(li)
                heapq.heappush(heap, (nums[li] + nums[i], li))
            bad += is_bad(i)
            if rj < n:
                heapq.heappush(heap, (nums[i] + nums[rj], i))

            ops += 1

        return ops