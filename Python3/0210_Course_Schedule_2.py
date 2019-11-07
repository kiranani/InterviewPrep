from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, deg = defaultdict(set), defaultdict(int)
        for course, prereq in prerequisites:
            graph[prereq].add(course)
            deg[course] += 1
        i, ans = 0, [None] * numCourses
        deg_0 = [i for i in range(numCourses) if i not in deg]
        while deg_0:
            n = deg_0.pop()
            ans[i], i = n, i + 1
            for c in graph[n]:
                deg[c] -= 1
                if deg[c] == 0:
                    deg_0.append(c)
        if i < numCourses:
            return []
        return ans
                    
        
