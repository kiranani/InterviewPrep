class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        holding, profit = -prices[0], 0
        for price in prices[1:]:
            sell = price + holding - fee
            profit = profit if profit > sell else sell
            buy = profit - price
            holding = holding if holding > buy else buy
        return profit
               
