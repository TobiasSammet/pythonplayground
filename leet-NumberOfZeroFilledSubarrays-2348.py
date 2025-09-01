from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        retVal: int = 0
        prevZeroes: int = 0
        for item in nums:
            if item == 0:
                retVal += prevZeroes + 1
                prevZeroes += 1
            else:
                prevZeroes = 0

        return retVal
    

thingy = Solution()

print(thingy.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4])) # 6
print(thingy.zeroFilledSubarray([0, 0, 0, 2, 0, 0])) # 9
print(thingy.zeroFilledSubarray([1,2,3])) # 0
print(thingy.zeroFilledSubarray([0, 1, 3, 0, 0, 2, 0, 0, 4])) # 7
# print(thingy.zeroFilledSubarray()) # 