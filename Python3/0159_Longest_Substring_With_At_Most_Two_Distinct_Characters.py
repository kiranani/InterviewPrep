class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r, n, h, m = 0, 0, len(s), collections.defaultdict(int), 0
        while r < n:
            while r < n and len(h) < 3:
                h[s[r]] += 1
                r += 1
            if r == n and len(h) < 3: 
                m = max(m, r - l)
                break
            else: 
                m = max(m, r - l - 1)
            while l < r and len(h) > 2:
                if h[s[l]] == 1:
                    del h[s[l]]
                else:
                    h[s[l]] -= 1
                l += 1
        return m
        
