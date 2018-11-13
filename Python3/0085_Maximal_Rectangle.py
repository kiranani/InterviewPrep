class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        def findMax(row, index):
            if row[index] == 0:
                return 0
            else:
                s, i = row[index], index - 1
                while i > -1 and row[i] >= row[index]:
                    s += row[index]
                    i -= 1
                i = index + 1
                while i < n and row[i] >= row[index]:
                    s += row[index]
                    i += 1
                return s
        ans, accu = 0, [0] * n
        for row in matrix:
            for j in range(n):
                if row[j] == "0":
                    accu[j] = 0
                else:
                    accu[j] += 1
            #print(accu)
            for j in range(n):
                s = findMax(accu, j)
                ans = ans if ans > s else s
        return ans
