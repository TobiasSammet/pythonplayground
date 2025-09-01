from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        values: List[int] = []
        for i in range(0, len(nums)):
            if nums[i] == key:
                values.append(i)
        if len(values) == 0:
            return []
        retVal: List[int] = []

        for i in range(0, len(nums)):
            j: int = 0
            while j < len(values):
                if abs(i - values[j]) <= k:
                    retVal.append(i)
                    break
                j +=1
        return retVal
    


thingy = Solution()

print(thingy.findKDistantIndices([3,4,9,1,3,9,5], 9, 1)) # [1,2,3,4,5,6]