class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        holding, profit = prices[0], 0
        for price in prices[1:]:
            sell = price - holding
            profit = profit if profit > sell else sell
            holding = holding if holding < price else price
        return profit
    
