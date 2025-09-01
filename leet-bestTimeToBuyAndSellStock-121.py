from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        bestBuy: int = prices[0]
        bestProfit: int = 0
        for i in range(1, len(prices)) :
            if prices[i] < bestBuy :
                bestBuy = prices[i]
            if (prices[i] - bestBuy) > bestProfit :
                bestProfit = prices[i] - bestProfit
        return bestProfit

prices: List[int] = [7,1,5,3,6,4]
thing = Solution()
print(thing.maxProfit(prices))