from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        retVal: int = 0
        bitwiseOr: int = self.calcTheOr(nums)
        
        for i in range(0, len(nums)):
            retVal += self.looper(nums[i], [], nums[:][i:], bitwiseOr)

        return retVal
    
    def looper(self, valToAdd: int, currentVal: List[int], numberPool: List[int], orValue) -> int:
        retVal: int = 0
        currentVal.append(valToAdd)
        if self.calcTheOr(currentVal) == orValue:
            retVal += 1
        newNumberPool = numberPool[:][1:]
        if len(newNumberPool) == 0:
            return retVal
        
        for i in range(0, len(newNumberPool)):
            retVal += self.looper(newNumberPool[i], currentVal[:], newNumberPool[:][i:], orValue)
        
        return retVal

    def calcTheOr(self, nums: List[int]) -> int:
        retVal: int = 0
        for num in nums:
            retVal = retVal | num
        return retVal

thingy = Solution()

print(thingy.countMaxOrSubsets([3,1])) # 2
print(thingy.countMaxOrSubsets([2,2,2])) # 7
print(thingy.countMaxOrSubsets([3,2,1,5])) # 6
# print(thingy.countMaxOrSubsets())
