class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not numCourses:
            return []
        graph = [[] for i in range(numCourses)]
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
        visited, courses = [0] * numCourses, []

        def dfs(course):
            if visited[course] == 1:
                return False
            elif visited[course] == 2:
                return True
            else:
                visited[course] += 1
                for node in graph[course]:
                    if not dfs(node):
                        return False
                visited[course] += 1
                courses.append(course)
                return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return courses
                
        
