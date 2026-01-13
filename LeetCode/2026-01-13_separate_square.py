# Problem: Split Squares by Horizontal Line
# Topic: Binary Search / Geometry
# Date: 13-01-2026

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_diff(y):
            below = 0.0
            above = 0.0
            for _, yi, l in squares:
                bottom = yi
                top = yi + l
                if y <= bottom:
                    above += l * l
                elif y >= top:
                    below += l * l
                else:
                    below += (y - bottom) * l
                    above += (top - y) * l
            return below - above

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):
            mid = (low + high) / 2
            if area_diff(mid) < 0:
                low = mid
            else:
                high = mid

        return low
