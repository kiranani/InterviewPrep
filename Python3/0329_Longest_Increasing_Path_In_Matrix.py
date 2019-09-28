class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n, dirs = len(matrix), len(matrix[0]), [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dp = [[0] * n for _ in range(m)]
        def dfs(i, j):
            if -1 < i < m and -1 < j < n:
                if dp[i][j] > 0:
                    return dp[i][j]
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if (-1 < ni < m and -1 < nj < n and 
                        matrix[i][j] < matrix[i + di][j + dj]):
                        dp[i][j] = max(dp[i][j], dfs(i + di, j + dj))
                dp[i][j] += 1
                return dp[i][j]
            return 0
        c = 0
        for i in range(m):
            for j in range(n):
                c = max(c, dfs(i, j))
        return c
                
        
