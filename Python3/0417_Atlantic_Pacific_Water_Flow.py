class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def pr(dp):
            for row in dp:
                print(row)
        if not matrix:
            return []
        ans = []
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(matrix), len(matrix[0])
        pacifica = [[False for j in range(n)] for i in range(m)]
        atlantic = [[False for j in range(n)] for i in range(m)]
        def dfs(dp, i, j):            
            for ni, nj in dirs:
                ni, nj = i + ni, j + nj
                if -1 < ni < m and -1 < nj < n and not dp[ni][nj] and matrix[i][j] <= matrix[ni][nj]:
                    dp[ni][nj] = True
                    dfs(dp, ni, nj)
        for j in range(n):
            if not pacifica[0][j]:
                pacifica[0][j] = True
                dfs(pacifica, 0, j)
            if not atlantic[-1][j]:
                atlantic[-1][j] = True
                dfs(atlantic, m - 1, j)
        for i in range(m):
            if not pacifica[i][0]:
                pacifica[i][0] = True
                dfs(pacifica, i, 0)
            if not atlantic[i][-1]:
                atlantic[i][-1] = True
                dfs(atlantic, i, n - 1)
        for i in range(m):
            for j in range(n):
                if atlantic[i][j] and pacifica[i][j]:
                    ans.append([i, j])
        return ans
