class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = [set() for i in range(n)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        nodes = set(range(n))
        while len(nodes) > 2:
            visited = [False] * n
            for i in range(n):
                if len(graph[i]) == 1 and not visited[i]:
                    nei = graph[i].pop()
                    graph[nei].remove(i)
                    nodes.remove(i)
                    visited[nei] = True
        return list(nodes)
