from typing import List

class Solution:
    def FindMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentCount: int = 0
        retVal: int = 0
        
        for num in nums:
            if num == 1:
                currentCount += 1
                retVal = max(currentCount, retVal)
            else:
                currentCount = 0
        return retVal

    
thing = Solution()
nums: List[int] = [1,1,0,1,1,1]
print(thing.FindMaxConsecutiveOnes(nums))