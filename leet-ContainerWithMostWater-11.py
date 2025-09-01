from typing import List

class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        retVal: int = 0
        for i in height :
            for j in range(i+1, len(height),1) :
                temp = min(height[i], height[j]) * (j - i)
                if temp > retVal: 
                    retVal = temp
        return retVal


thing = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(thing.maxArea(height))