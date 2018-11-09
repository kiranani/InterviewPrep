class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            row = [1] + [0] * (i - 1) + [1]
            for j in range(1, i):
                row[j] = ans[-1][j - 1] + ans[-1][j]
            ans.append(row)
        return ans
