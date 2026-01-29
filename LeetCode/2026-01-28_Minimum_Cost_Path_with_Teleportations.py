import heapq
import collections

class Solution:
    def minCost(self, grid, k):
        INF = 10 ** 20
        R = len(grid)
        C = len(grid[0])

        cells = []
        for i in range(R):
            for j in range(C):
                cells.append((grid[i][j], i, j))

        cells.sort()
        q = [collections.deque(cells) for _ in range(k + 1)]

        best = [[[INF] * (k + 1) for _ in range(C)] for _ in range(R)]
        best[0][0][k] = 0

        h = []
        heapq.heappush(h, (0, 0, 0, k))

        directions = [(1, 0), (0, 1)]

        while h:
            d, x, y, ck = heapq.heappop(h)

            if best[x][y][ck] != d:
                continue

            if x == R - 1 and y == C - 1:
                return d

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    nd = d + grid[nx][ny]
                    if best[nx][ny][ck] > nd:
                        best[nx][ny][ck] = nd
                        heapq.heappush(h, (nd, nx, ny, ck))

            if ck > 0:
                while q[ck] and q[ck][0][0] <= grid[x][y]:
                    _, nx, ny = q[ck][0]
                    q[ck].popleft()

                    if best[nx][ny][ck - 1] > d:
                        best[nx][ny][ck - 1] = d
                        for nk in range(ck - 2, -1, -1):
                            best[nx][ny][nk] = d
                        heapq.heappush(h, (d, nx, ny, ck - 1))

        return -1
