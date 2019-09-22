class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n > 2:
            i = 1
            while i < n and A[i] > A[i - 1]:
                i += 1
            if i == 1 or i == n:
                return False
            while i < n and A[i] < A[i - 1]:
                i += 1
            if i == n:
                return True
        return False
                
        
