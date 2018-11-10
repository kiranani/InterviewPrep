class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def pr(dp):
            for d in dp:
                print(d)
        m = len(grid)
        if m == 0:
            return 0
        n, kills = len(grid[0]), -float("inf")
        dp = [[0] * n for _ in range(m)]
        u, d = [0] * n, [0] * n
        for i in range(m):
            r, l = 0, 0
            for j in range(n):
                if grid[i][j] == "E":
                    l += 1
                    u[j] += 1
                elif grid[i][j] == "W":
                    l, u[j] = 0, 0
                else:
                    dp[i][j] += l + u[j]
                    kills = kills if dp[i][j] < kills else dp[i][j]
                x, y = -i - 1, -j - 1
                if grid[x][y] == "E":
                    r += 1
                    d[y] += 1
                elif grid[x][y] == "W":
                    r, d[y] = 0, 0
                else:
                    dp[x][y] += r + d[y]
                    kills = kills if dp[x][y] < kills else dp[x][y]
        #pr(dp)
        return kills if kills > 0 else 0
