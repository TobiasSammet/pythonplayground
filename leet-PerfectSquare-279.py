from typing import List
import sys
class QuickSolution:
    def numSquares(self, n: int) -> int:
        nums: List[int] = []
        i: int = 1
        while i*i <= n:
            nums.append(i*i)
            i += 1
        currentLevel: List[int] = [n]
        nextLevel: List[int] = []
        retVal: int = 0
        while True:
            retVal += 1
            for val in currentLevel:
                for num in nums:
                    if val - num == 0:
                        return retVal
                    if val - num > 0:
                        nextLevel.append(val-num)
            currentLevel = nextLevel.copy()
        return retVal

class Solution:
    masterCount: int
    def numSquares(self, n: int) -> int:
        self.masterCount = sys.maxsize
        nums: List[int] = self.calcSquares(n)
        for num in nums:
            self.calcNum(n, num, nums, 0)
        return self.masterCount

    def calcNum(self, n: int, currentNum: int, nums: List[int], currentCount: int) -> None :
        temp: int = n - currentNum
        currentCount += 1
        if temp == 0:
            self.masterCount = min(self.masterCount, currentCount)
            return
        if temp > 0 :
            for num in nums:
                self.calcNum(temp, num, nums, currentCount)

    def calcSquares(self, n: int) -> List[int]:
        nums: List[int] = []
        i: int = 1
        while i*i <= n:
            nums.append(i*i)
            i += 1
        return nums        


thing = Solution()
print(thing.numSquares(1))
print(thing.numSquares(12))
print(thing.numSquares(13))