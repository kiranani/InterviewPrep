class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rots, fresh, dirs = set(), 0, [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                    rots.add((i, j))
        if not fresh:
            return 0
        t = -1
        while rots:
            new_rots = set()
            for i, j in rots:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if -1 < ni < m and  -1 < nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 0
                        new_rots.add((ni, nj))
                        fresh -= 1
            t, rots = t + 1, new_rots
        return -1 if fresh else t
