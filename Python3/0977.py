from collections import deque
class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        i, j, k, ans = 0, n - 1, n - 1, [None] * n
        while k > -1:
            iSq, jSq = A[i] ** 2, A[j] ** 2
            if iSq < jSq:
                ans[k] = jSq
                j -= 1
            else:
                ans[k] = iSq
                i += 1
            k -= 1
        return ans
        
