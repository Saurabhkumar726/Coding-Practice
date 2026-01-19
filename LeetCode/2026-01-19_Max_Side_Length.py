from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pref[i + 1][j + 1] = (
                    pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                    + mat[i][j]
                )

        def square_sum(x, y, k):
            return (
                pref[x + k][y + k]
                - pref[x][y + k]
                - pref[x + k][y]
                + pref[x][y]
            )

        low, high = 0, min(m, n)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            found = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if square_sum(i, j, mid) <= threshold:
                        found = True
                        break
                if found:
                    break

            if found:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

        