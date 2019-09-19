class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def smaller(x):
            c, i, j = 0, 0, n - 1
            while i < n and j > -1:
                if matrix[i][j] < x:
                    c += j + 1
                    i += 1
                else:
                    j -= 1
            return c
        def bs():
            low, high = matrix[0][0], matrix[n - 1][n - 1]
            while low <= high:
                mid = (low + high) // 2
                s = smaller(mid)
                if s >= k:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        return bs()
        
