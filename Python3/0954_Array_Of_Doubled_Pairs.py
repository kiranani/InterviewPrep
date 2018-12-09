class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        d = collections.Counter(A)
        for k in sorted(A):
            n = d[k]
            if n > 0:
                if k / 2 in d and d[k / 2] > 0:
                    d[k] -= 1
                    d[k / 2] -= 1
                elif 2 * k in d and d[2 * k] > 0:
                    d[k] -= 1
                    d[2 * k] -= 1
                else:
                    return False
        return True
