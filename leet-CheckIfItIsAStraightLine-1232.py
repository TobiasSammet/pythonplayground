from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 1:
            return False
        if len(coordinates) == 2:
            return True
        masterSlope= self.calcSlope(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
        for i in range(2,len(coordinates)) :
            tempSlope = self.calcSlope(coordinates[0][0], coordinates[0][1], coordinates[i][0], coordinates[i][1])
            if tempSlope != masterSlope :
                return False
        
        return True

    def calcSlope(self, x1: int, y1: int, x2:int , y2: int) -> int :
        numerator: int = y2-y1
        denominator: int = x2 -x1
        return numerator / denominator

thing = Solution()
coordinates: List[List[int]] = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(thing.checkStraightLine(coordinates)) # true
coordinates2: List[List[int]] = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(thing.checkStraightLine(coordinates2)) # false
