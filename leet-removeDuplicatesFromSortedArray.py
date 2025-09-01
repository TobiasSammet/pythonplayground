from typing import List

class Solution :
    def removeDuplicates(self, nums: List[int]) -> int :
        if len(nums) <= 1:
            return len(nums)
        temp: int = nums[0]
        retVal: int = 1
        for i in range(1, len(nums)):
            if nums[i] != temp :
                nums[retVal] = nums[i]
                retVal += 1
                temp = nums[i]
        return retVal

thing = Solution()
nums: List[int] = [0,0,1,1,1,2,2,3,3,4]
print(thing.removeDuplicates(nums))
print(nums)