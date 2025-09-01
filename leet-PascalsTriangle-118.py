from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[]]
        if numRows == 1:
            return [[1]]
        retVal: List[List[int]] = []
        retVal.append([1])
        retVal.append([1,1])
        for i in range(3, numRows+1):
            currentRow: List[int] = []
            currentRow.append(1)
            for j in range(0,i-2):
                temp: int = retVal[i-2][j] + retVal[i-2][j+1]
                # print(temp)
                currentRow.append(temp)
            currentRow.append(1)
            retVal.append(currentRow)
        return retVal

thingy = Solution()

# print(thingy.generate(1))
# print(thingy.generate(2))

print(thingy.generate(3))
print(thingy.generate(4))


# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(thingy.generate(5))