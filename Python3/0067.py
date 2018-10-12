class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        h = {"0": 0, "1": 1}
        aN, bN = len(a), len(b)
        if aN > bN:
            aN, bN, a, b = bN, aN, b, a
        ans, c = collections.deque(), 0
        for i in range(aN):
            digit = c + h[a[-i - 1]] + h[b[-i - 1]]
            c, digit = digit // 2, digit % 2
            ans.appendleft(str(digit))
        for i in range(bN - aN):
            digit = c + h[b[-i - 1 - aN]]
            c, digit = digit // 2, digit % 2
            ans.appendleft(str(digit))
        if c:
            ans.appendleft(str(c))
        return "".join(ans)
