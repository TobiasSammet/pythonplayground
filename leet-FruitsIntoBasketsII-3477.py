from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        retVal:int = 0
        basketInUse: List[int] = [False] * len(baskets)
        for fruit in fruits:
            used: bool = False
            for i in range(0, len(baskets)):
                if (basketInUse[i] == False) and (baskets[i] >= fruit):
                    used = True
                    basketInUse[i] = True
                    break
            if used == False:
                retVal += 1
        return retVal
    


thingy = Solution()

print(thingy.numOfUnplacedFruits([4, 2, 5], [3, 5, 4])) # 1
print(thingy.numOfUnplacedFruits([3, 6, 1], [6, 4, 7])) # 0
# print(thingy.numOfUnplacedFruits())
# print(thingy.numOfUnplacedFruits())