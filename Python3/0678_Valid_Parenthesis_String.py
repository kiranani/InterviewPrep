class Solution:
    def checkValidString(self, s: str) -> bool:
        l = h = 0
        for c in s:
            if c == "(":
                l, h = l + 1, h + 1
            elif c == ")":
                l, h = l - 1, h - 1
            else:
                l, h = l - 1, h + 1
            if h < 0:
                return False
            if l < 0:
                l = 0
        return l == 0
        
