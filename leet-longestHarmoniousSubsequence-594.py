from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        retVal: int = 0
        currentNum: int = nums[0]
        currentNumCount: int = 1
        nextNumCount: int = 0
        i: int = 1
        while(i <len(nums)):
            if nums[i] == currentNum:
                currentNumCount += 1
                i += 1
            elif nums[i] == currentNum + 1:
                while i < len(nums) and nums[i] == currentNum + 1 :
                    nextNumCount += 1
                    i += 1
                retVal = max(retVal, nextNumCount + currentNumCount)
                currentNum += 1
                currentNumCount = nextNumCount
                nextNumCount = 0
            else:
                currentNum = nums[i]
                currentNumCount = 1
                nextNumCount = 0
                i += 1

        return retVal
        
    

thingy = Solution()

print(thingy.findLHS([1,3,2,2,5,2,3,7])) # 5
print(thingy.findLHS([1,2,3,4])) # 2
print(thingy.findLHS([1,1,1,1])) # 0
print(thingy.findLHS([0,3,1,3,3,3,0,1,0,2,0,3,1,3,-3,2,0,3,1,2,2,-3,2,2,3,3])) # 15
# print(thingy.findLHS([])) #