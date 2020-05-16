from heapq import heapify, heappop, heappush
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        dirs, ineligible = [(-1, 0), (1, 0), (0, -1), (0, 1)], set()
        def dfs_ineligible(i, j):
            ineligible.add((i, j))
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if (-1 < ni < m and -1 < nj < n 
                    and heightMap[i][j] <= heightMap[ni][nj] 
                    and (ni, nj) not in ineligible):
                    dfs_ineligible(ni, nj)
        for i in range(m):
            dfs_ineligible(i, 0)
            dfs_ineligible(i, n - 1)
        for j in range(1, n - 1):
            dfs_ineligible(0, j)
            dfs_ineligible(m - 1, j)
            
        mn = m * n
        if len(ineligible) == mn:
            return 0
        
        boundary = []
        for i, j in ineligible:
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if -1 < ni < m and -1 < nj < n and (ni, nj) not in ineligible:
                    boundary.append((heightMap[i][j], i, j))
                    break
        heapify(boundary)
        
        visited, total = set(), 0
        def dfs_collect(h, i, j):
            total = 0
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if -1 < ni < m and -1 < nj < n:
                    if (ni, nj) not in ineligible and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        if h >= heightMap[ni][nj]:
                            total += h - heightMap[ni][nj]
                            total += dfs_collect(h, ni, nj)
                        else:
                            heappush(boundary, (heightMap[ni][nj], ni, nj))
            return total
        while len(ineligible) + len(visited) < mn:
            total += dfs_collect(*heappop(boundary))
        return total
            
                
