class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return False
        i = 0
        while i < n - 1 and A[i] < A[i + 1]:
            i += 1
        if i == n - 1 or i == 0:
            return False
        while i < n - 1 and A[i] > A[i + 1]:
            i += 1
        return i == n - 1
        
