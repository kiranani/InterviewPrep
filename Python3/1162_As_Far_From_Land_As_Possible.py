class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        m, n, d = len(grid), len(grid[0]), 0
        q, dirs = set(), [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if -1 < ni < m and -1 < nj < n and grid[ni][nj]:
                            q.add((i, j))
                            break
        if not q:
            return -1
        while q:
            temp_q = set()
            for i, j in q:
                grid[i][j] = 1
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if (-1 < ni < m and -1 < nj < n 
                        and not grid[ni][nj] and (ni, nj) not in q):
                        temp_q.add((ni, nj))
            q = temp_q
            d += 1
        return d
        
        
