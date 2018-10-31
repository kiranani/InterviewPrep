class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == ""
        match = s != "" and (p[0] == s[0] or p[0] == ".")
        if len(p) >= 2 and p[1] == "*":
            return (match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        else:
            return match and self.isMatch(s[1:], p[1:])
                             
