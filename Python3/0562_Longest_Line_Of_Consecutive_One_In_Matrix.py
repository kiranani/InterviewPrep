class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        m, n, m_ij = len(M), len(M[0]), 0
        dp = [[0] * 4 for _ in range(n)]
        for i in range(m):
            ndp = [[M[i][j]] * 4 for j in range(n)]
            for j in range(n):
                if M[i][j]:
                    ndp[j][1] += dp[j][1]
                    if j > 0:
                        ndp[j][0] += ndp[j - 1][0]
                        ndp[j][2] += dp[j - 1][2]
                    if j < n - 1:
                        ndp[j][3] += dp[j + 1][3]
                    m_ij = max(m_ij, max(ndp[j]))
            dp = ndp
        return m_ij
                    
                    
