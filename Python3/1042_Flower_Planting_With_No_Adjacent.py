from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for n1, n2 in paths:
            graph[n1].add(n2)
            graph[n2].add(n1)
        colours = {1, 2, 3, 4}
        ans = [None] * N
        for i in range(1, N + 1):
            ans[i - 1] = (colours - {ans[x - 1] for x in graph[i]}).pop()
        return ans
