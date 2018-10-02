class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        i, j = 0, n - 1
        while i <= j:
            m = (i + j) // 2
            if citations[m] == (n - m):
                return n - m
            elif citations[m] < (n - m):
                i = m + 1
            else:
                j = m - 1
        return n - i
