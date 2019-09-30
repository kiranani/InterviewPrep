class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        lr, hr, lc, hc = -1, m, -1, n
        d, dirs = 0, [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, r, c, ans = 0, 0, 0, [0] * m * n
        while i < m * n:
            while lr < r < hr and lc < c < hc:
                ans[i] = matrix[r][c]
                i, r, c = i + 1, r + dirs[d][0], c + dirs[d][1]
            if d == 0:
                lr, r, c = lr + 1, r + 1, c - 1
            elif d == 1:
                hc, r, c = hc - 1, r - 1, c - 1
            elif d == 2:
                hr, r, c = hr - 1, r - 1, c + 1
            else:
                lc, r, c = lc + 1, r + 1, c + 1
            d = (d + 1) % 4
        return ans
        
