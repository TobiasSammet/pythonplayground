from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        retVal: List[int] = []        
        ascending = False

        for i in range(cols):
            temp :List[int] = []
            currentCol = i
            currentRow = 0
            while (currentRow < rows) and (currentCol >=0):
                temp.append(mat[currentRow][currentCol])
                currentRow += 1
                currentCol -= 1
            if ascending:
                retVal.extend(temp)
                ascending = False
            else :
                temp.reverse()
                retVal.extend(temp)
                ascending = True
        # print(retVal)
        
        for i in range(1, rows):
            temp :List[int] = []
            currentCol = cols-1
            currentRow = i
            while (currentRow < rows) and (currentCol >=0):
                temp.append(mat[currentRow][currentCol])
                currentRow += 1
                currentCol -= 1
            if ascending:
                retVal.extend(temp)
                ascending = False
            else :
                temp.reverse()
                retVal.extend(temp)
                ascending = True
        

        return retVal
    

thingy = Solution()

print(thingy.findDiagonalOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]))
print(thingy.findDiagonalOrder([[3,2,1]])) # [3,2,1]
print(thingy.findDiagonalOrder([[3],[2],[1]])) # [3,2,1]
print(thingy.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,4,7,5,3,6,8,9]
print(thingy.findDiagonalOrder([[1,2],[3,4]])) # [1,2,3,4]
# print(thingy.findDiagonalOrder()) # 
# print(thingy.findDiagonalOrder()) # 
# print(thingy.findDiagonalOrder()) # 
# print(thingy.findDiagonalOrder()) # 
# print(thingy.findDiagonalOrder()) # 