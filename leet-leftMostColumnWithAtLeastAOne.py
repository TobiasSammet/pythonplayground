from typing import List

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    data: List[int] =  []
    dimension: int
    def __init__(self, i: int) :
        if i == 1 :
            self.dimension = 2
            ##create and prefill two dimensional array
            for i in range(self.dimension) :
                column: List[int] = []
                for j in range(self.dimension) :
                    column.append(0)
                self.data.append(column)
            # now that is is filled in we can simply modify values
            self.data[1][0] = 1
            self.data[1][1] = 1


    def get(self, x: int, y: int) -> int:
        return self.data[x][y]
    def dimensions(self) -> List[int]:
        retVal: List[int] = []
        retVal.append(self.dimension)
        retVal.append(self.dimension)
        return retVal

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        foundOne: bool = False
        length: int = binaryMatrix.dimensions()[0]
        width: int = binaryMatrix.dimensions()[1]
        posX: int = 0
        posY: int = width
        while posX < length :
            if binaryMatrix.get(posX, posY -1) == 1 :
                foundOne = True
                posY -= 1
                if posY == 0:
                    return 0
            else :
                posX +=1
        if foundOne == True :
            return posY
        return -1

thing = Solution()
binaryMatrix = BinaryMatrix(1)
print(thing.leftMostColumnWithOne(binaryMatrix))