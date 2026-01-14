from typing import List
from bisect import bisect_left

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        xs = sorted(xs)
        x_index = {v: i for i, v in enumerate(xs)}

        events.sort()
        cover = [0] * (len(xs) - 1)

        def union_length():
            total = 0
            for i, c in enumerate(cover):
                if c > 0:
                    total += xs[i + 1] - xs[i]
            return total

        slices = []
        prev_y = events[0][0]
        active_len = 0
        total_area = 0
        i = 0

        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy > 0 and active_len > 0:
                area = active_len * dy
                slices.append((prev_y, y, active_len, area))
                total_area += area

            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                for xi in range(x_index[x1], x_index[x2]):
                    cover[xi] += typ
                i += 1

            active_len = union_length()
            prev_y = y

        half = total_area / 2
        acc = 0

        for y1, y2, length, area in slices:
            if acc + area >= half:
                return y1 + (half - acc) / length
            acc += area

        return 0.0
