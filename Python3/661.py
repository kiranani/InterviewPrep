class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(M), len(M[0])
        N = []
        for i in range(r):
            N.append([0] * c)
        if r == 1 and c == 1:
            N[0][0] = M[0][0]
            return N
        if r == 1:
            for j in range(1, c - 1):
                N[0][j] = (M[0][j - 1] + M[0][j] + M[0][j + 1]) // 3
            N[0][0] = (M[0][0] + M[0][1]) // 2
            N[0][-1] = (M[0][-2] + M[0][-1]) // 2
            return N
        if c == 1:
            for i in range(1, r - 1):
                N[i][0] = (M[i - 1][0] + M[i][0] + M[i + 1][0]) // 3
            N[0][0] = (M[0][0] + M[1][0]) // 2
            N[-1][0] = (M[-1][0] + M[-2][0]) // 2
            return N
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                N[i][j] = M[i][j - 1] + M[i][j + 1]
                N[i][j] += M[i - 1][j] + M[i + 1][j]
                N[i][j] += M[i - 1][j - 1] + M[i + 1][j + 1]
                N[i][j] += M[i - 1][j + 1] + M[i + 1][j - 1]
                N[i][j] = (N[i][j] + M[i][j]) // 9
        for i in range(1, r - 1):
            N[i][0] = M[i - 1][0] + M[i + 1][0] + M[i][1]
            N[i][0] += M[i - 1][1] + M[i + 1][1] + M[i][0]
            N[i][0] = N[i][0] // 6
            N[i][-1] = M[i - 1][-1] + M[i + 1][-1] + M[i][-2]
            N[i][-1] += M[i - 1][-2] + M[i + 1][-2] + M[i][-1]
            N[i][-1] = N[i][-1] // 6
        for j in range(1, c - 1):
            N[0][j] = M[0][j - 1] + M[0][j + 1] + M[0][j]
            N[0][j] += M[1][j - 1] + M[1][j + 1] + M[1][j]
            N[0][j] = N[0][j] // 6
            N[-1][j] = M[-1][j - 1] + M[-1][j + 1] + M[-2][j]
            N[-1][j] += M[-2][j - 1] + M[-2][j + 1] + M[-1][j]
            N[-1][j] = N[-1][j] // 6
        N[0][0] = (M[0][0] + M[1][1] + M[0][1] + M[1][0]) // 4
        N[0][-1] = (M[0][-1] + M[0][-2] + M[1][-1] + M[1][-2]) // 4
        N[-1][0] = (M[-1][0] + M[-1][1] + M[-2][0] + M[-2][1]) // 4
        N[-1][-1] = (M[-1][-1] + M[-1][-2] + M[-2][-1] + M[-2][-2]) // 4
        return N
