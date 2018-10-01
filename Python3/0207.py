class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def courseDone(course, pre, visited, queued):
            #print(course, queued)
            if visited[course]:
                return True
            if queued[course]:
                return False
            queued[course] = True
            for preReq in pre[course]:
                if not courseDone(preReq, pre, visited, queued):
                    return False
            visited[course], queued[course] = True, False
            return True
        
        pre = [set() for x in range(numCourses)]
        for pair in prerequisites:
            pre[pair[0]].add(pair[1])
        #print(pre)
        visited = [False] * numCourses
        queued = [False] * numCourses
        for course in range(numCourses):
            if not courseDone(course, pre, visited, queued):
                return False
        return True
