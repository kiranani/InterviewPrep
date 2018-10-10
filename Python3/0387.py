class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = collections.Counter(s)
        for i, c in enumerate(s):
            if h[c] == 1:
                return i
        return -1
