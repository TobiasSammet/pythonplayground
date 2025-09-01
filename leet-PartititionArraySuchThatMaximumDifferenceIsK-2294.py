from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if len(nums) <=1:
            return len(nums)
        nums.sort()
        print(nums)
        retVal: int = 1
        currentValue: int = nums[0]

        i: int = 1
        while i < len(nums):
            if nums[i] > currentValue + k:
                retVal += 1
                currentValue = nums[i]   
            i+= 1        
        
        return retVal
    


thingy = Solution()

print(thingy.partitionArray([3,6,1,2,5], 2)) # 2

print(thingy.partitionArray([1,2,3],1)) # 2
print(thingy.partitionArray([2,2,4,5],0)) #3
# print(thingy.partitionArray([],))
# print(thingy.partitionArray([],))