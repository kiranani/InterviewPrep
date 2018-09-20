class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        N = len(grid)
        max_col, max_row = [0] * N, [0] * N
        for i in range(N):
            for j in range(N):
                val = grid[i][j]
                if val > 0:
                    area += 1
                max_col[i] = val if val > max_col[i] else max_col[i]
                max_row[j] = val if val > max_row[j] else max_row[j]
        return area + sum(max_row) + sum(max_col)
