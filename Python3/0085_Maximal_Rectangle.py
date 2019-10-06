class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        mx, dp = 0, [0] * n
        for row in matrix:
            ndp = [0] * n
            for j in range(n):
                if row[j] == "1":
                    ndp[j] = dp[j] + 1
            dp = ndp
            s = [-1]
            for i, e in enumerate(dp):
                while s[-1] != -1 and e <= dp[s[-1]]:
                    mx = max(mx, dp[s.pop()] * (i - s[-1] - 1))
                s.append(i)
            while s[-1] != -1:
                mx = max(mx, dp[s.pop()] * (n - s[-1] - 1))
        return mx
            
        
