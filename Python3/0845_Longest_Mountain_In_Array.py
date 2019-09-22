class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n, i, si, mi, m, inc = len(A), 0, 0, 0, 0, True
        if n < 3:
            return 0
        while i + 1 < n:
            if inc:
                while i + 1 < n and A[i + 1] > A[i]:
                    i += 1
                mi = i
                inc = False
            else:
                while i + 1 < n and A[i + 1] < A[i]:
                    i += 1
                inc = True
                if i - si > 1 and si < mi < i:
                    m = max(m, i - si + 1)
                elif i + 1 < n and A[i + 1] == A[i]:
                    i += 1
                si, mi = i, i
        return m
        
