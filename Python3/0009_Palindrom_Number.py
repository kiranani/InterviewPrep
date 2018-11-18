class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x):
            return False
        p, y = 0, x
        while y:
            r, y = y % 10, y // 10
            p = 10 * p + r
        return p == x
        
