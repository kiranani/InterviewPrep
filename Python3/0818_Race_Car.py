class Solution:
    def racecar(self, target: int) -> int:
        if (target & (target + 1) == 0): 
            return target.bit_length()
        dp = [float("inf")] * (target + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, target + 1):
            if (i & (i + 1)) == 0:
                dp[i] = i.bit_length()
                continue
            k = i.bit_length()
            for j in range(k - 1):
                d = k + j + 1 + dp[i - ((1 << k - 1) - (1 << j))]
                dp[i] = min(dp[i], d)
            dp[i] = min(dp[i], dp[(1 << k) - i - 1] + k + 1)
        return dp[target]
        
