from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        retVal: int = 0
        currentValue: int = 0
        maxValue = max(nums)
        i: int = 0
        while i < len(nums):
            if nums[i] == maxValue:
                while i < len(nums) and nums[i] == maxValue:
                    currentValue += 1
                    retVal = max(retVal, currentValue)
                    i += 1
                currentValue = 0
            else :
                i+= 1
        return retVal
    

thingy = Solution()

print(thingy.longestSubarray([1, 2, 3, 3, 2, 2])) # 2
print(thingy.longestSubarray([1, 2, 3, 4])) #1
# print(thingy.longestSubarray()) #
# print(thingy.longestSubarray()) #