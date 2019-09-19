class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        elif n < 4:
            return max(nums)
        dp = [(0, nums[0]), (0, nums[~0])]
        for i in range(1, n - 1):
            dp[0] = max(dp[0]), dp[0][0] + nums[i]
            dp[1] = max(dp[1]), dp[1][0] + nums[~i]
        return max(max(dp[0]), max(dp[1]))
        
