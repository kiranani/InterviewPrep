from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        c, visited = 0, set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for c in graph[node]:
                    dfs(c)
        for i in range(n):
            if i not in visited:
                c += 1
                dfs(i)
        return c
        
