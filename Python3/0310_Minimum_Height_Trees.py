from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3:
            return list(range(n))
        graph = defaultdict(set)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        deg_1 = [k for k in graph if len(graph[k]) == 1]
        while n > 2:
            n -= len(deg_1)
            temp = []
            for node in deg_1:
                for c in graph[node]:
                    graph[c].remove(node)
                    if len(graph[c]) == 1:
                        temp.append(c)
            deg_1 = temp
        return deg_1
        
