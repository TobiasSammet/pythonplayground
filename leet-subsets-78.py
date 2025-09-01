from typing import List

class Solution :
    def subsets(self, nums: List[int]) -> List[List[int]] :
        retVal: List[List[int]] = []
        retVal.append([])
        for num in nums :
            myLength = len(retVal)
            for i in range(myLength):
                mySet = retVal[i].copy()
                mySet.append(num)
                retVal.append(mySet)
        return retVal

thing = Solution()
nums: List[int] = [1,2,3]
print(thing.subsets(nums))