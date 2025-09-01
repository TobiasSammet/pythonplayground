from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return -1
        retVal: int = -1
        minVal: int = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= minVal:
                minVal = nums[i]
            else:
                retVal = max(retVal, nums[i]-minVal)
        
        if retVal < 0:
            return -1
        return retVal
    

thingy = Solution()

print(thingy.maximumDifference([7,1,5,4])) # 4
print(thingy.maximumDifference([9,4,3,2])) # -1
print(thingy.maximumDifference([1,5,2,10])) # 9