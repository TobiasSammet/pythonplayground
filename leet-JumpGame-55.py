from typing import List

class Solution :
    def canJump(self, nums: List[int]) -> bool :
        canGetHere: List[bool] = [False] * len(nums)
        canGetHere[0] = True
        for i in range(0, len(nums)):
            if canGetHere[i] : 
                value: int = nums[i]
                for j in range(1, value + 1)  :
                    if (i+j) < len(nums) :
                        canGetHere[i+j] = True
        return canGetHere[len(canGetHere) -1]

thing = Solution()
nums: List[int] = [2,3,1,1,4]
print(thing.canJump(nums))
nums2: List[int] = [3,2,1,0,4]
print(thing.canJump(nums2))