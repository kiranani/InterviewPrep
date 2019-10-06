class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n, dirs = len(A), len(A[0]), [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def dfs(visited, i, j):
            if -1 < i < m and -1 < j < n and A[i][j] and (i, j) not in visited:
                visited.add((i, j))
                for dx, dy in dirs:
                    dfs(visited, i + dx, j + dy)
        def bfs(q, l, visited):
            nei = set()
            for i, j in q:
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if -1 < ni < m and -1 < nj < n and (ni, nj) not in visited:
                        if A[ni][nj]:
                            return l, nei
                        visited.add((ni, nj))
                        nei.add((ni, nj))
            return 0, nei
        island = set()
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    dfs(island, i, j)
                    break
            if island:
                break
        b, l, q = 0, 0, set(island)
        while l == 0:
            l, q = bfs(q, b, island)
            b += 1
        return l
        
        
