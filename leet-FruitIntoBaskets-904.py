from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        retVal: int = 0
        i: int = 0
        while i < len(fruits) -1:
            temp = self.grabFromCurrent(fruits, i)
            retVal = max(retVal, temp[0])
            i = temp[1]
            if i == -1: 
                break
        return retVal

    def grabFromCurrent(self, fruits: List[int], startSpot: int) -> tuple[int, int]:
        if startSpot > len(fruits):
            return [0,-1]
        retVal: int = 1
        firstBasket:int = fruits[startSpot]
        spotOfSecondBasket: int = -1
        secondBasket:int = -1
        i: int = startSpot + 1
        while i < len(fruits):
            if ((fruits[i] == firstBasket) or (fruits[i] == secondBasket)):
                retVal += 1
                i +=1
            elif secondBasket == -1:
                spotOfSecondBasket = i
                secondBasket = fruits[i]
                retVal += 1
                i += 1
            else:
                break
        return [retVal, spotOfSecondBasket]

    

thingy = Solution()


print(thingy.totalFruit([1,2,1])) # 3
print(thingy.totalFruit([0,1,2,2])) #3
print(thingy.totalFruit([1,2,3,2,2])) # 4
# print(totalFruit())
# print(totalFruit())