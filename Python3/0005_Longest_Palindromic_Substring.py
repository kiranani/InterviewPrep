class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n, maxL, maxS = len(s), 0, []
        if n < 2:
            return s
        dp = [0] + [1 if c == s[-1] else 0 for i, c in enumerate(s)]
        for i in range(2, n + 1):
            #print(dp)
            ndp = [0] * (n + 1)
            for j in range(n):
                if s[j] == s[-i]:
                    ndp[j + 1] = dp[j] + 1
                    if ndp[j + 1] > maxL and s[j] == s[j - ndp[j + 1] + 1]:
                        maxL = ndp[j + 1]
                        maxS = [j - ndp[j + 1] + 1, j]
            dp = ndp
        return s[maxS[0]: maxS[1] + 1]
