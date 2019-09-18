class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, n1, n2, n = 0, len(num1), len(num2), collections.deque()
        if n2 < n1:
            n1, n2, num1, num2 = n2, n1, num2, num1
        c = 0
        while i < n1:
            c, r = divmod(c + int(num1[~i]) + int(num2[~i]), 10)
            n.appendleft(str(r))
            i += 1
        while i < n2:
            c, r = divmod(c + int(num2[~i]), 10)
            n.appendleft(str(r))
            i += 1
        if c:
            n.appendleft(str(c))
        return "".join(n)
