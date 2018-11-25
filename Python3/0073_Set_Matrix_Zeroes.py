class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def pr():
            for row in matrix:
                print(row)
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        firstRowZero = any(x == 0 for x in matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i and matrix[i][0]:
                        matrix[i][0] = 0
                    if matrix[0][j]:
                        matrix[0][j] = 0
        #pr()
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
                
