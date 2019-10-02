class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        dp = collections.defaultdict(int)
        m, n, c = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for k in range(j):
                        if grid[i][k]:
                            c += dp[k, j]
                            dp[k, j] += 1
        return c
        
