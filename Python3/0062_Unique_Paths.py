class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        state = [1] * n
        for i in range(1, m):
            newState = [1] + [0] * (n - 1)
            for j in range(1, n):
                newState[j] = state[j] + newState[j - 1]
            state = newState
        print(state)
        return state[-1]
        
