class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def dfs(rooms, visited, index):
            if not visited[index]:
                visited[index] = True
                for key in rooms[index]:
                    dfs(rooms, visited, key)
        visited = [False] * len(rooms)
        dfs(rooms, visited, 0)
        #print(visited)
        return all(x for x in visited)
