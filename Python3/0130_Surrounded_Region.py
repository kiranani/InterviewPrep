class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n, dirs = len(board), len(board[0]), [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(i, j):
            if -1 < i < m and -1 < j < n and board[i][j] == "O":
                board[i][j] = 1
                for di, dj in dirs:
                    dfs(i + di, j + dj)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == 1:
                    board[i][j] = "O"
                
        
