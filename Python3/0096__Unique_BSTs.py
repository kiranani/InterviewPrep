class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            iby2 = i // 2
            for j in range(iby2):
                dp[i] += 2 * dp[j] * dp[i - j - 1]
            if i & 1:
                dp[i] += dp[iby2] ** 2
        return dp[n]
        
