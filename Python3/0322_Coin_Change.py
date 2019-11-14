class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        INF = float("inf")
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != INF else -1
        
