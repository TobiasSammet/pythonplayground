from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        retVal: int = nums[0]
        starter: int = 0
        rollingSum: int = nums[0]
        setThing: set = {nums[0]}

        for i in range(1, len(nums)):
            if nums[i] in setThing:
                while nums[i] in setThing:
                    setThing.remove(nums[starter])
                    rollingSum -= nums[starter]
                    starter += 1
            setThing.add(nums[i])
            rollingSum += nums[i]
            retVal = max(retVal, rollingSum)
        return retVal

    

thingy = Solution()
print(thingy.maximumUniqueSubarray([4, 2, 4, 5, 6])) # 17
print(thingy.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5])) # 8
print(thingy.maximumUniqueSubarray([10000])) # 10000
# print(thingy.maximumUniqueSubarray()) 