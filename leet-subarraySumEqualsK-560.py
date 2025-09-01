from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup: List[int] = []
        retVal: int = 0
        tempSum: int = 0
        for i in range(len(nums)):
            tempSum += nums[i]
            lookup.append(tempSum)
        
        for i in range(len(nums)) :
            currentVal = lookup[i]
            if currentVal == k:
                retVal = retVal + 1
            for j in range(i-1, -1,-1) :
                if currentVal - lookup[j] == k :
                    retVal = retVal + 1
        return retVal

thing = Solution()
nums: List[int] = [1,1,1,2]
print(thing.subarraySum(nums, 2))