class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minA, minB = m, n
        for a, b in ops:
            minA = min(a, minA)
            minB = min(b, minB)
        return minA *  minB
        
