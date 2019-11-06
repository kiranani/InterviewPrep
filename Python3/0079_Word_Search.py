class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return not word
        m, n, wn = len(board), len(board[0]), len(word)
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        def dfs(i, j, wi):
            if wi == wn:
                return True
            elif -1 < i < m and -1 < j < n and word[wi] == board[i][j]:
                board[i][j] = "#"
                for di, dj in dirs:
                    if dfs(i + di, j + dj, wi + 1):
                        return True
                board[i][j] = word[wi]
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
    
        
