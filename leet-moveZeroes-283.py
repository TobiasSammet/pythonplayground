from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1 : 
            return
        count = nums.count(0)
        if count > 0 :
            currentIndex: int = 0
            for i in range(0,len(nums)) :
                if nums[i] != 0 :
                    nums[currentIndex] = nums[i]
                    currentIndex += 1
            for i in range(len(nums) - count, len(nums)) :
                nums[i] = 0

            
        

thing = Solution()
nums: List[int] = [0,1,0,4,3]
thing.moveZeroes(nums)
print(nums)