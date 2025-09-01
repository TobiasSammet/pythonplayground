from typing import List
import math 
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonalLength = 0
        retVal = 0
        for item in dimensions:
            if len(item) == 2:
                temp = math.sqrt(item[0] * item[0] + item[1] * item[1])
                if temp >= diagonalLength:
                    if temp == diagonalLength:
                        retVal = max(retVal, item[0] * item[1])
                    else:
                        retVal = item[0] * item[1]
                    diagonalLength = temp
        return retVal
thingy = Solution()

# print(thingy.areaOfMaxDiagonal([[9,3],[8,6]])) # 48
# print(thingy.areaOfMaxDiagonal([[3,4],[4,3]])) # 12
print(thingy.areaOfMaxDiagonal([
    [6, 5],
    [8, 6],
    [2, 10],
    [8, 1],
    [9, 2],
    [3, 5],
    [3, 5],
  ])) # 20

# print(thingy.areaOfMaxDiagonal()) # 
# print(thingy.areaOfMaxDiagonal()) # 
# print(thingy.areaOfMaxDiagonal()) # 