class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        mn, mx = prices[0], 0
        for price in prices[1:]:
            if price < mn:
                mn = price
            elif price - mn > mx:
                mx = price - mn
        return mx
        
