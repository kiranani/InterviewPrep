class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(1, L + 1):
            ndp = [0] * (N + 1)
            for j in range(1, N + 1):
                ndp[j] = dp[j - 1] * (N + 1 - j)
                ndp[j] += dp[j] * max(j - K, 0)
            dp = ndp
        return dp[N] % (10 ** 9 + 7)
        
