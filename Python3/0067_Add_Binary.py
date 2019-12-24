class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na, nb = len(a), len(b)
        if na > nb:
            na, nb = nb, na
            a, b = b, a
        c, ans = 0, collections.deque()
        i = 0
        while i < na:
            c, r = divmod(c + int(a[~i]) + int(b[~i]), 2)
            ans.appendleft(str(r))
            i += 1
        while i < nb:
            c, r = divmod(c + int(b[~i]), 2)
            ans.appendleft(str(r))
            i += 1
        if c:
            ans.appendleft(str(c))
        return "".join(ans)
        
