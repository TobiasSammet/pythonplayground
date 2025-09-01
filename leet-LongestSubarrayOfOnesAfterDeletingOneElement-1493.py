from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length: int = len(nums)
        if 0 not in nums:
            return length -1 
        lastZero: int = -1
        retVal: int = 0
        i: int = -1

        while i < length:
            i+= 1
            if nums[i] == 0:
                lastZero = i
                break
            retVal = i + 1

        startOfWindow = i
        currentCount = retVal

        for i in range(lastZero+1, length):
            if nums[i] == 1:
                currentCount += 1
            else:
                currentCount = i - (lastZero + 1)
                lastZero = i
            retVal = max(retVal, currentCount)

        return retVal
    

thingy = Solution()

print(thingy.longestSubarray([1,1,0,1])) # 3
print(thingy.longestSubarray([0,1,1,1,0,1,1,0,1])) # 5
print(thingy.longestSubarray([1,1,1])) # 2
# print(thingy.longestSubarray()) # 