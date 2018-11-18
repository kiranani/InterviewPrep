class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        m, n = len(A), len(A[0])
        c = 0
        for j in range(n):
            for i in range(m - 1):
                if A[i][j] > A[i + 1][j]:
                    c += 1
                    break
        return c
            
