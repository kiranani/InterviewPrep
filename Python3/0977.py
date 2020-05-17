from collections import deque
class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = deque()
        i, j = 0, len(A) - 1
        while i <= j:
            iSq, jSq = A[i] ** 2, A[j] ** 2
            if iSq < jSq:
                ans.appendleft(jSq)
                j -= 1
            else:
                ans.appendleft(iSq)
                i += 1
        return ans
        
