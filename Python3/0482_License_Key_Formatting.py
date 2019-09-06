class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()
        n = len(S)
        i, j, ans = 0, n % K, []
        if j == 0:
            j = K
        while i < n:
            ans.append(S[i:j])
            i, j = j, j + K
        return "-".join(ans)
        
        
        
