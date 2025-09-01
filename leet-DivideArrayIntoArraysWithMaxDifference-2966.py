from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0:
            return []
        retVal: List[List[int]] = []
        nums.sort()
        # print(nums)
        i: int = 0
        while i < len(nums)-1:
            if nums[i+2] - nums[i] > k:
                return []
            retVal.append([nums[i], nums[i+1], nums[i+2]])
            i+=3
        return retVal

thingy = Solution()

# print(thingy.divideArray([1,3,4,8,7,9,3,5,1], 3))
print(thingy.divideArray([2,4,2,2,5,2], 2))
# print(thingy.divideArray([4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14))
# print(thingy.divideArray([33, 26, 4, 18, 16, 24, 24, 15, 8, 18, 34, 20, 24, 16, 3], 16))
# print(thingy.divideArray())