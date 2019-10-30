class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if abs(n1 - n2) > 1:
            return False
        if n1 > n2:
            n1, n2, s, t = n2, n1, t, s
        for i in range(n1):
            if s[i] != t[i]:
                if n1 == n2:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        return n1 < n2
        
