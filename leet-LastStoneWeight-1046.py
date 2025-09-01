from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1 :
            stone1 = self.findHeaviestStone(stones)
            stone2 = self.findHeaviestStone(stones)
            newStone = self.crushStones(stone1, stone2)
            if newStone != 0 :
                stones.append(newStone)
        
        if len(stones) == 1 :
            return stones[0]

        return 0

    def crushStones(self, stone1: int, stone2: int) -> int:
        return abs(stone1-stone2)

    def findHeaviestStone(self, stones: List[int]) -> int:
        retVal = max(stones)
        stones.remove(retVal)
        return retVal

thing = Solution()
stones: List[int] = [2,7,1,8,1]

print(thing.lastStoneWeight(stones))