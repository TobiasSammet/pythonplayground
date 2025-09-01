# 119. Pascal's Triangle II
# Easy

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]


from typing import List

def printList(cells: List[int]) -> str :
    retVal: str = ""
    for value in cells:
        retVal += " " + str(value)
    return retVal.strip()

class Solution :
    
    def getRow(self, row: int) -> List[int]:
        thing = self.generate(row + 1)
        return thing[-1]
    
    def generate(self, numRows: int) -> List[List[int]] :
        retVal: List[List[int]] = []
        if (numRows <= 0) :
            return retVal
        val: int = 1
        
        for i in range(numRows) :
            currentRow: List[int] = []
            for j in range(0, i + 1) :
                if j == 0 or i == 0 :
                    val = 1
                else :
                    val = val * (i-j + 1) // j
                currentRow.append(val)
            retVal.append(currentRow)
        return retVal
    

thing = Solution()
print(thing.generate(4))
print(thing.getRow(30))