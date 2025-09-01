from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        retVal: int = 0
        for i in range(1, len(prices)) :
            if prices[i] > prices[i-1] :
                retVal += prices[i] - prices[i-1]
        return retVal

prices: List[int] = [7,1,5,3,6,4]
thing = Solution()
print(thing.maxProfit(prices))