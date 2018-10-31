class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for child in graph[node]:
                dfs(child)
        c, visited = 0, [False] * n
        for node in range(n):
            if not visited[node]:
                c += 1
                dfs(node)
        return c
    
