class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        norm, a = ord("A") - 1, collections.deque()
        while n != 0:
            m, n = n % 26, (n - 1) // 26
            m = m if m > 0 else 26
            a.appendleft(chr(m + norm))
        return "".join(a)
