class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m, n = len(S), len(T)
        dp = list(range(m + 1))
        for i, t in enumerate(T):
            ndp = [-1] * (m + 1)
            for j, s in enumerate(S):
                if t == s:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = ndp[j]
            dp = ndp
        mn, lr = float("inf"), (0, 0)
        for i in range(1, m + 1):
            if dp[i] > -1 and i - dp[i] < mn:
                mn, lr = i - dp[i], (dp[i], i)
        return S[lr[0]:lr[1]]
        
                
        
