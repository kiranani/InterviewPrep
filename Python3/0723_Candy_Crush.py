class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n, s, changed = len(board), len(board[0]), set(), False
        for i in range(m):
            l, r = 0, 0
            while r < n:
                while r < n and board[i][r] == 0:
                    r += 1
                l = r
                while r < n and board[i][l] == board[i][r]:
                    r += 1
                if r - l > 2:
                    changed = True
                    while l < r:
                        board[i][l] = -board[i][l]
                        l += 1
                else:
                    l = r
        for j in range(n):
            u, d = 0, 0
            while d < m:
                while d < m and board[d][j] == 0:
                    d += 1
                u = d
                while d < m and abs(board[u][j]) == abs(board[d][j]):
                    d += 1
                if d - u > 2:
                    changed = True
                    while u < d:
                        board[u][j] = -abs(board[u][j])
                        u += 1
                else:
                    u = d
            i = 0
            for v in range(m):
                if board[~v][j] > 0:
                    board[~i][j] = board[~v][j]
                    i += 1
            for i in range(m - i):
                board[i][j] = 0
        return board if not changed else self.candyCrush(board)
                        
        
