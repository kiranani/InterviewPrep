class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet, n = set(wordDict), len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            for i in range(j):
                if dp[i] and s[i:j] in wordSet:
                    dp[j] = True
                    break
        return dp[n]
        
