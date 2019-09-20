class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n, shapes = len(grid), len(grid[0]), set()
        def dfs(i, j, d):
            if -1 < i < m and -1 < j < n and grid[i][j]:
                shape.append(str(d))
                grid[i][j] = 0
                dfs(i - 1, j, d + 1)
                dfs(i, j - 1, d + 2)
                dfs(i + 1, j, d + 3)
                dfs(i, j + 1, d + 4)
        for i in range(m):
            for j in range(n):
                shape = []
                dfs(i, j, 0)
                if shape:
                    shapes.add("".join(shape))
        return len(shapes)
        
        
