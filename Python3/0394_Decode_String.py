class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        def helper(s, i):
            m, a = 0, ""
            while i < n:
                c = s[i]
                if c.isdigit():
                    m = 10 * m + int(c)
                elif c.isalpha():
                    a += c
                elif c == "[":
                    r, i = helper(s, i + 1)
                    a, m = a + m * r, 0
                else:
                    return a, i
                i += 1
            return a, i
        return helper(s, 0)[0]
        
