class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n, buildings = len(grid), len(grid[0]), 0
        reached, distance = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(i, j):
            d = 1
            v, nei = set(), set([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
            while nei:
                temp = set()
                for ni, nj in nei:
                    if -1 < ni < m and -1 < nj < n and grid[ni][nj] == 0:
                        v.add((ni, nj))
                        reached[ni][nj] += 1
                        distance[ni][nj] += d
                        for di, dj in dirs:
                            ndi, ndj = ni + di, nj + dj
                            if (ndi, ndj) not in v:
                                temp.add((ndi, ndj))
                nei = temp
                d += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1
                    bfs(i, j)
        md = float("inf")
        for i in range(m):
            for j in range(n):
                if reached[i][j] == buildings:
                    md = min(md, distance[i][j])
        return md if md != float("inf") else -1
                        
        
