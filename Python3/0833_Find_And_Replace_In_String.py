class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        s = list(S)
        def fix_s(s, t, m, k):
            i, j, n = k, 0, len(t)
            if m == n:
                s[k:k + m] = t
            elif m < n:
                s[k:k + m] = t[:m]
                s[k + m - 1] += t[m:]
            else:
                s[k:k + n] = t
                s[k + n:k + m] = [""] * (m - n)
                
        for i, index in enumerate(indexes):
            m = len(sources[i])
            if sources[i] == S[index:index + m]:
                fix_s(s, targets[i], m, index)
        return "".join(s)
                
        
