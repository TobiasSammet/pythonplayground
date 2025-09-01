from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k==0 :
            return
        retVal: List[int] = [None] * len(nums)
        for i in range(len(nums)) :
            retVal[(i + k) % len(nums)] = nums[i]
        for i in range(len(nums)) :
            nums[i] = retVal[i]
        
        
thing = Solution()
nums: List[int] = [1,2,3,4,5,6,7]
thing.rotate(nums, 3)
print(nums)
