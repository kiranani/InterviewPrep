class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        state = [x for x in grid[0]]
        for i in range(1, n):
            state[i] += state[i - 1]
        for i in range(1, m):
            newState = [grid[i][0] + state[0]] + [0] * (n - 1)
            for j in range(1, n):
                newState[j] = grid[i][j] + min(newState[j - 1], state[j])
            state = newState
        return state[-1]
        
