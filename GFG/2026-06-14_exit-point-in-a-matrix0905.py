class Solution:
    def exitPoint(self, mat):
        n = len(mat)
        m = len(mat[0])

        i = j = 0
        direction = 0  # 0=right, 1=down, 2=left, 3=up

        while 0 <= i < n and 0 <= j < m:
            if mat[i][j] == 1:
                direction = (direction + 1) % 4
                mat[i][j] = 0

            if direction == 0:
                j += 1
            elif direction == 1:
                i += 1
            elif direction == 2:
                j -= 1
            else:
                i -= 1

        if i < 0:
            i += 1
        elif i >= n:
            i -= 1
        elif j < 0:
            j += 1
        else:
            j -= 1

        return [i, j]