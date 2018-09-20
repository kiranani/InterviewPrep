class Solution:
    def getPaths(self, start, graph):
        if start == len(graph) - 1:
            return [[start]]
        paths = []
        for s in graph[start]:
            if s > start:
                pPaths = self.getPaths(s, graph)
                for path in pPaths:
                    if (len(graph) - 1) in path:
                        paths.append([start] + path)
        return paths
    def allPathsSourceTarget(self, graph):
        return self.getPaths(0, graph)
    
