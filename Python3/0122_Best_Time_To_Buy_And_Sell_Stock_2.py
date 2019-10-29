class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit, holding = 0, -prices[0]
        for price in prices[1:]:
            sell = price + holding
            profit = profit if profit > sell else sell
            buy = profit - price
            holding = holding if holding > buy else buy
        return profit
        
