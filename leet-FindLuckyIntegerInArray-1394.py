from typing import List
# 4ms
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        retVal: int = -1
        i: int = 0
        while i < len(arr):
            currentValue: int = arr[i]
            currentCount: int = 0
            while (i < len(arr)) and (arr[i] == currentValue):
                currentCount += 1
                i += 1
            if currentCount == currentValue:
                retVal = currentValue
        return retVal

thingy = Solution()
print(thingy.findLucky([2,2,2,3,3]))
print(thingy.findLucky([2,2,3,4]))
print(thingy.findLucky([1,2,2,3,3,3]))
# print(thingy.findLucky([]))