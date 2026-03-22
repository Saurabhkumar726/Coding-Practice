from collections import deque

class Solution:
    def orangesRot(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        fresh_count = 0
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    queue.append((i, j, 0))
                elif mat[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        max_time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y, time = queue.popleft()
            max_time = max(max_time, time)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] == 1:
                    mat[nx][ny] = 2
                    fresh_count -= 1
                    queue.append((nx, ny, time + 1))
        
        return max_time if fresh_count == 0 else -1