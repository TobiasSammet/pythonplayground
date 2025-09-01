from typing import List

class Solution :
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurrent = nums[0]
        maxGlobal = nums[0]
        for i in range(1, len(nums)) :
            if maxCurrent + nums[i] > nums[i] :
                maxCurrent += nums[i]
            else :
                maxCurrent = nums[i]
            
            if maxCurrent > maxGlobal :
                maxGlobal = maxCurrent

        return maxGlobal

thing = Solution()
nums: List[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(thing.maxSubArray(nums))