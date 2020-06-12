class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def isValid(i, j):
            return -1 < i < m and  -1 < j < n
        q, fresh, dirs = set(), 0, [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                    q.add((i, j))
        if not fresh:
            return 0
        t = -1
        while q:
            n_q = set()
            for i, j in q:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if isValid(ni, nj) and grid[ni][nj] == 1:
                        grid[ni][nj] = 0
                        n_q.add((ni, nj))
                        fresh -= 1
            t, q = t + 1, n_q
        return -1 if fresh else t
