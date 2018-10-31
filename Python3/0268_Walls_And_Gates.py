class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m, n, I = len(rooms), len(rooms[0]), 2147483647
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i, j])
        while len(q) > 0:
            ij = q.popleft()
            for d in dirs:
                i, j = ij[0] + d[0], ij[1] + d[1]
                #print(i, j)
                if -1 < i < m and -1 < j < n and rooms[i][j] == I:
                    #print(q)
                    q.append([i, j])
                    rooms[i][j] = 1 + rooms[ij[0]][ij[1]]
