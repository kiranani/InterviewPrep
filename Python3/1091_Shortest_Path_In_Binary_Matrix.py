class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n and not grid[0][0]:
            dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), 
                    (1, 1), (1, 0), (1, -1), (0, -1)]
            q, grid[0][0] = [(0, 0, 1)], 1
            for i, j, d in q:
                if i == n - 1 and j == n - 1:
                    print(q)
                    return d
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if -1 < ni < n and -1 < nj < n and not grid[ni][nj]:
                        grid[ni][nj] = 1
                        q.append((ni, nj, d + 1))
        return -1
        
