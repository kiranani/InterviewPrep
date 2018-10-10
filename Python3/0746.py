class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def recurse(cost, index, h):
            if index >= len(cost):
                return 0
            if h.get(index):
                return h[index]
            oneStep = recurse(cost, index + 1, h)
            twoStep = recurse(cost, index + 2, h)
            h[index] = cost[index] + min(oneStep, twoStep)
            return h[index]
        h = {}
        recurse(cost, 0, h)
        recurse(cost, 1, h)
        return min(h[0], h[1])
        
