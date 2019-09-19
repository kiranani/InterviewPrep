class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m - 1):
            j = 0
            while i + 1 < m and j + 1 < n:
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
                i, j = i + 1, j + 1
        for j in range(n - 1):
            i = 0
            while i + 1 < m and j + 1 < n:
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
                i, j = i + 1, j + 1
        return True
        
