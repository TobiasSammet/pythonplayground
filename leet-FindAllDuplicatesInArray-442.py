from typing import List

class Solution :
    def findDuplicates(self, nums: List[int]) -> List[int] :
        retVal: List[int] = []
        nums.sort()
        x: int = -9999
        for num in nums:
            if num == x:
                retVal.append(num)
            else:
                x= num
        return retVal

thing = Solution()
nums: List[int] = [4,3,2,7,8,2,3,1]
print(thing.findDuplicates(nums))