class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, h = len(s), {}
        m = l = 0
        for r, c in enumerate(s):
            if c not in h or h[c] < l:
                m = max(m, r - l + 1)
            else:
                l = h[c] + 1
            h[c] = r
        return m
        
        
