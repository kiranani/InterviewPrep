class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(n, c):
            if n in visited:
                return c == visited[n]
            visited[n] = c
            c = (c + 1) % 2
            for nei in graph[n]:
                if not dfs(nei, c):
                    return False
            return True
        visited = {}
        for n in range(len(graph)):
            if n not in visited and not dfs(n, 0):
                return False
        return True
        
