class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        def dfs(node, parent):
            if visited[node]:
                return False
            visited[node] = True
            for child in graph[node]:
                if child != parent and not dfs(child, node):
                    return False
            return True
        visited = [False] * n
        if not dfs(0, None):
            return False
        return all(x for x in visited)
