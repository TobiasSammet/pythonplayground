# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.
# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

# Example 1:
# Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# Output: 3
# Explanation: The largest magic square has a size of 3.
# Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
# - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
# - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
# - Diagonal sums: 5+4+3 = 6+4+2 = 12

# Example 2:
# Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# Output: 2
# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 50
#     1 <= grid[i][j] <= 106

# just brute for on this one :(

from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rowCount: int = len(grid)
        colCount: int = len(grid[0])
        testSize: int = min(rowCount, colCount)
        if testSize <=1:
            return testSize
        while testSize > 1:
            for i in range(0, rowCount - testSize + 1):
                for j in range(0, colCount - testSize + 1):
                    if self._isMagicSquare(i,j,testSize, grid):
                        return testSize
            testSize -= 1
        
        return 1
    
    def _isMagicSquare(self, row: int, col: int, size: int, grid: List[List[int]]) -> bool:
        value: int = -1
        tempValue: int = 0
        # rows
        for currentRow in range(row, row+size):
            tempValue = 0
            for i in range(0, size):
                tempValue += grid[currentRow][col+i]
            if value == -1:
                value = tempValue
            else:
                if tempValue != value:
                    return False
        #cols
        for currentCol in range(col, col+size):
            tempValue = 0
            for i in range(0, size):
                tempValue += grid[row+i][currentCol]
            if tempValue == -1:
                value = tempValue
            else:
                if tempValue != value:
                    return False                        

        # top left to lower right diag
        tempValue = 0
        for offset in range(0, size):
            tempValue += grid[row + offset][col + offset];

        if tempValue != value:
            return False
        
        # bottom left to upper right diag
        tempValue = 0
        for offset in range(size-1, -1, -1):
            tempValue += grid[row + offset][col + size - offset - 1]

        if tempValue != value:
            return False

        return True    

def main(): 
    thingy = Solution()
    assert thingy.largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]) == 3, "Test Case 1 failed"
    assert thingy.largestMagicSquare([[5,1,3,1],[9,3,3,1],[1,3,3,8]]) == 2, "Test Case 2 failed"
    assert thingy.largestMagicSquare([[1,17,15,17,5,16,8,9],[1,19,11,18,8,18,3,18],[6,6,5,8,3,15,6,11],[19,5,6,11,9,2,14,13],[12,16,16,15,14,18,10,7],[3,11,15,15,7,1,9,8],[15,5,11,17,18,20,14,17],[13,17,7,20,12,2,13,19]]) == 1, "Test Case 3 failed"    
    # assert thingy.largestMagicSquare() == 1, "Test Case X failed"    

if __name__ == "__main__":
    main()    