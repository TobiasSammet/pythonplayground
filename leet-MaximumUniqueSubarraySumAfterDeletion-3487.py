from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        retVal: int = 0
        lastNum: int = float('-inf')
        biggestNum: int = nums[0]
        for item in nums:
            if item > 0:
                if item != lastNum:
                    retVal += item
                    lastNum = item
            if item > biggestNum:
                biggestNum = item
        if biggestNum < 0:
            retVal += biggestNum
        return retVal
    

thingy = Solution()

print(thingy.maxSum([1, 2, 3, 4, 5])) # 15
print(thingy.maxSum([1, 1, 0, 1, 1])) # 1
print(thingy.maxSum([1, 2, -1, -2, 1, 0, -1])) #3
print(thingy.maxSum([-100])) 
print(thingy.maxSum([-17, -15])) 