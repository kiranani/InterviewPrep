class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        p, m, n = 0, len(grid), len(grid[0])
        def isValid(ni, nj):
            return -1 < ni < m and -1 < nj < n
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    e = 4
                    for d in dirs:
                        ni, nj = i + d[0], j + d[1]
                        if isValid(ni, nj):
                            e -= grid[ni][nj]
                    p += e
        return p
        
        
