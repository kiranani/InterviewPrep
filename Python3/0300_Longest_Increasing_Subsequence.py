class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [nums[0]]
        def bs(t):
            l, r = 0, len(dp)
            while l <= r:
                m = (l + r) // 2
                if dp[m] == t:
                    return m
                elif t < dp[m]:
                    r = m - 1
                else:
                    l = m + 1
            return l
        for num in nums[1:]:
            if num > dp[-1]:
                dp.append(num)
            else:
                dp[bs(num)] = num
        return len(dp)
