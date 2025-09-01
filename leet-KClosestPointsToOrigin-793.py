from typing import List
from math import pow

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        retVal: List[List[int]] = []
        myHT = {}
        if len(points) <= K:
            return points
        for i in range(len(points)):
            temp = points[i]
            if len(temp) == 2:
                calcValue: int = pow(temp[0],2) + pow(temp[1],2)
                myHT[i] = calcValue
        s = sorted(myHT.items(), key=lambda x: x[1])
        for i in range(K):
            retVal.append(s[i])

        return retVal



thing = Solution()
points: List[List[int]] = [[3, 3],[5,-1],[-2,4]]
print(thing.kClosest(points, 2))
