from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        if rows == 0:
            return 0
        if cols == 0: 
            return 0
        retVal: int = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    retVal = max(retVal, 1)
                    tempSize: int = 2
                    while True:
                        if self.isSquare(matrix, i, j, tempSize):
                            retVal = max(retVal, tempSize)
                        else :
                            break
                        tempSize = tempSize + 1
    
        return retVal * retVal
    
    
    
    def isSquare(self, matrix: List[List[str]], row: int, col: int, size: int) -> bool:
        if (row + size -1 ) >= len(matrix) :
             return False
        if (col + size -1) >= len(matrix[0]):
            return False
        for i in range(size) :
            for j in range(size) :
                if matrix[row + i][col + j] == "0":
                    return False
        return True


thing = Solution()    
# matrix: List[List[str]] = [
#     ["1", "1"],
#     ["1", "1"]
# ]
matrix: List[List[str]] = [
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0'],
]
# print(thing.isSquare(matrix,0,0,1))
# print(thing.isSquare(matrix,0,0,2))
# print(thing.isSquare(matrix,0,0,3))
# print(thing.isSquare(matrix,1,1,1))
# print(thing.isSquare(matrix,1,1,2))


print(thing.maximalSquare(matrix))