class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def pr(dp):
            for d in dp:
                print(d)
        n1, n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] + ord(s2[i - 1])
        #pr(dp)
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        #pr(dp)
        return dp[n1][n2]
