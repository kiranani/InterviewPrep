class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt, lt = collections.Counter(t), len(t)
        si = [(i, s[i]) for i in range(len(s)) if s[i] in dt]
        n, l, r, m, ij, lf = len(si), 0, 0, float("inf"), (0, 0), 0
        d = collections.defaultdict(int)
        while r < n:
            while r < n and lf < lt:
                i, c = si[r]
                d[c] += 1
                if d[c] <= dt[c]:
                    lf += 1
                r += 1
            while l < n and lf == lt:
                i, j, c = si[l][0], si[r - 1][0] + 1, si[l][1]
                d[c] -= 1
                if j - i < m:
                    ij, m = (i, j), j - i
                if d[c] < dt[c]:
                    lf -= 1
                l += 1
        return s[ij[0]:ij[1]]
        
                
        
