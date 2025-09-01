from typing import List

    

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if k<=0: 
            return []
        theNums = [(i, num) for i, num in enumerate(nums)]
        theNums.sort(key=lambda item: -item[1])
        keepers : List[(int, int)] = []
        for i in range(k):
            keepers.append(theNums[i])
        keepers.sort(key=lambda item: item[0])
        retVal: List[int] = []
        for i in range(k):
            retVal.append(keepers[i][1])
        return retVal
    
thingy = Solution()

print(thingy.maxSubsequence([4, 3, 3], 2)) # [4,3]
# print(thingy.maxSubsequence(75, -50)) # [75,-50]


