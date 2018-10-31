class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d, l, m = {}, 0, 0
        for i, ch in enumerate(s):
            if d.get(ch) is None or d[ch] < l:
                m = m if m > i - l + 1 else i - l + 1
            else:
                l = d[ch] + 1
            d[ch] = i
        return m
