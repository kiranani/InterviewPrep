class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n, INF = len(maze), len(maze[0]), float("inf")
        q, dist = collections.deque([tuple(start)]), [[INF] * n for _ in range(m)]
        dirs, dist[start[0]][start[1]] = [(-1, 0), (0, 1), (1, 0), (0, -1)], 0
        while q:
            sx, sy = q.popleft()
            for i, j in dirs:
                c, x, y = 0, sx + i, sy + j
                while -1 < x < m and -1 < y < n and maze[x][y] == 0:
                    c, x, y = c + 1, x + i, y + j
                x, y = x - i, y - j
                if (dist[sx][sy] + c < dist[x][y] and 
                    dist[sx][sy] + c < dist[destination[0]][destination[1]]):
                    dist[x][y] = dist[sx][sy] + c
                    q.append((x, y))
        if dist[destination[0]][destination[1]] != INF:
            return dist[destination[0]][destination[1]]
        else:
            return -1
            
        
        
        
