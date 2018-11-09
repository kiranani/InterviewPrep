class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        state = [1]
        for i in range(1, rowIndex + 1):
            newState = [1] + [0] * (len(state) - 1) + [1]
            for j in range(1, i):
                newState[j] = state[j - 1] + state[j]
            state = newState
        return state
