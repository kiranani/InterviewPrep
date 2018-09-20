class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        d = {0: 1, 1: 0}
        def toggleRow(A, i):
            for j in range(c):
                A[i][j] = d[A[i][j]]
        r, c = len(A), len(A[0])
        cCount = [0] * c
        s, m = 0, 2 ** (c - 1)
        for i, row in enumerate(A):
            if row[0] == 0:
                toggleRow(A, i)
            for j in range(c):
                cCount[j] += A[i][j]
        for j in range(c):
            if cCount[j] < r / 2:
                cCount[j] = r - cCount[j]
            s += m * cCount[j]
            m //= 2
        return s
