class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, ans = ord("A") - 1, 0
        for c in s:
            ans = ans * 26 + ord(c) - n
        return ans
