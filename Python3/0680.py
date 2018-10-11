class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def recurse(s, limit):
            if limit < 0:
                return False
            if s == "":
                return True
            n = len(s)
            i, j = 0, n - 1
            while i < j:
                #print(s[i], s[j])
                if s[i] != s[j]:
                    return recurse(s[i:j], limit - 1) or recurse(s[i + 1: j + 1], limit - 1)
                else:
                    i += 1
                    j -= 1
            return True
        return recurse(s, 1)
        
