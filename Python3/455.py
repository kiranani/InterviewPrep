class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        gi, si, c = 0, 0, 0
        gn, sn = len(g), len(s)
        while gi < gn and si < sn:
            if g[gi] <= s[si]:
                c += 1
                gi += 1
                si += 1
            else:
                si += 1
        return c
        
