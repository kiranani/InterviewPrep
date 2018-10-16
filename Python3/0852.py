class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        i, j = 0, n - 1
        while i <= j:
            m = (i + j) // 2
            if A[m - 1] < A[m] > A[m + 1]:
                return m
            elif A[m - 1] < A[m] < A[m + 1]:
                i = m + 1
            elif A[m - 1] > A[m] > A[m + 1]:
                j = m - 1
