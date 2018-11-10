class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = triangle[0]
        for i, level in enumerate(triangle[1:]):
            #print(level)
            level[0] += dp[0]
            level[-1] += dp[-1]
            for j in range(i):
                level[j + 1] += min(dp[j], dp[j + 1])
            dp = level
        return min(dp)
        
