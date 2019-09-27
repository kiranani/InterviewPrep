class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, r, n, h, m = 0, 0, len(s), {}, 0
        while r < n:
            while r < n and len(h) <= k:
                h[s[r]] = r
                r += 1
            if len(h) > k:
                m = max(m, r - l - 1)
            else:
                m = max(m, r - l)
            while l < r and len(h) > k:
                d = min(h.values())
                del h[s[d]]
                l = d + 1
        return m
        
