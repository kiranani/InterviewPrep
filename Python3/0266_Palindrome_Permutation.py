class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = collections.Counter(s)
        odds = [c for c in h if h[c] % 2 == 1]
        if len(odds) > 1 or (len(odds) == 1 and len(s) % 2 == 0):
            return False
        return True
