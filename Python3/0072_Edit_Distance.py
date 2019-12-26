class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = list(range(l2 + 1))
        for i in range(l1):
            ndp = [0] * (l2 + 1)
            ndp[0] = i + 1
            for j in range(l2):
                if word1[i] == word2[j]:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = 1 + min(ndp[j], dp[j + 1], dp[j])
            dp = ndp
        return dp[-1]
        
