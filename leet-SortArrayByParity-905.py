from typing import List

class Solution :
    def sortArrayByParity(self, A: List[int]) -> List[int] :
        retVal: List[int] = []
        odds: List[int] = []
        for value in A:
            if value % 2 == 0:
                retVal.append(value)
            else:
                odds.append(value)

        retVal = retVal + odds
        return retVal
            

thing = Solution()
nums: List[int] = [3,1,2,4]
print(thing.sortArrayByParity(nums))