class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h, ss = {}, set()
        for i in range(len(s)):
            if not h.get(s[i]) and t[i] in ss:
                return False
            elif h.get(s[i]) and h[s[i]] != t[i]:
                return False
            h[s[i]] = t[i]
            ss.add(t[i])
        return True
