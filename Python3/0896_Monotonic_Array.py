class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return True
        inc = None
        for i in range(1, n):
            if A[i] > A[i - 1]:
                if inc is None:
                    inc = True
                elif inc is False:
                    return False
            elif A[i] < A[i - 1]:
                if inc is None:
                    inc = False
                elif inc is True:
                    return False
        return True
        
        
