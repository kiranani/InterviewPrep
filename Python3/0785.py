class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        d = {1: 2, 2: 1}
        def bfs(colour, graph, index, co):
            if colour[index] != 0 and colour[index] != co:
                return False
            colour[index] = co
            for nei in graph[index]:
                if colour[nei] == 0:
                    if not bfs(colour, graph, nei, d[co]):
                        return False
                else:
                    if colour[nei] != d[co]:
                        return False
            return True
            
        colour = [0] * len(graph)
        for i, nei in enumerate(graph):
            if colour[i] == 0:
                if not bfs(colour, graph, i, 1):
                    return False
        return True
