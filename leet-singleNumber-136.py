from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        theSet: [int] = []
        for num in nums :
            if num in theSet:
                theSet.remove(num)
            else :
                theSet.append(num)

        return theSet

thing = Solution()

nums: List[int] = [4,1,2,1,2,5]

print(thing.singleNumber(nums))
print('all done!')