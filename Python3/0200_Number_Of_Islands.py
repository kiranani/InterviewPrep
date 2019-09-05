class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        def dfs(i, j):
            if i > -1 and i < r and j > -1 and j < c and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i, j - 1)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i + 1, j)
        islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands
                
        
