class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n, dest = len(maze), len(maze[0]), tuple(destination)
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(x, y, v):
            if -1 < x < m and -1 < y < n and maze[x][y] == 0 and (x, y) not in v:
                v.add((x, y))
                reached = False
                for dx, dy in dirs:
                    nx, ny = x, y
                    while (-1 < nx + dx < m and -1 < ny + dy < n and 
                           maze[nx + dx][ny + dy] == 0):
                        nx, ny = nx + dx, ny + dy
                    if (nx, ny) == dest:
                        return True
                    elif dfs(nx, ny, v):
                        return True
            return False
        return dfs(*start, set())
        
