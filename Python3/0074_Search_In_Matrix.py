class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        r, c = len(matrix), len(matrix[0])
        n = r * c
        i, j = 0, n - 1
        while i <= j:
            m = (i + j) // 2
            x, y = m // c, m % c
            #print(i, j, x, y, c)
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                j = m - 1
            else:
                i = m + 1
        return False
            
        
