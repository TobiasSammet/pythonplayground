# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

# Example 1:
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:

#  4  3  8
#  9  5  1
#  2  7  6

# while this one is not:


#  3  8  4
#  5  1  9
#  7  6  2

# In total, there is only one magic square inside the given grid.

# Example 2:
# Input: grid = [[8]]
# Output: 0

# Constraints:
#     row == grid.length
#     col == grid[i].length
#     1 <= row, col <= 10
#     0 <= grid[i][j] <= 15

# turns out there is 1 magic grid where all the rows, columns and diagnals add up to the same value
# and that value is 15. This means 5 must be in the center of the grid
# we also need to check that all the number are used exactly once.


from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        length: int = len(grid)
        width: int = len(grid[0])
        if length < 3 or width < 3:
            return 0
        retVal: int = 0

        for i in range(1, length -1):
            for j in range (1, width -1):
                if grid[i][j] == 5:
                    badNums: bool = False
                    numbers: list[bool] = 9 * [False]
                    for x in range(-1, 2):
                        if badNums == False:
                            for y in range(-1, 2):
                                tempNum = grid[i + x][j + y]
                                if tempNum <= 0 or tempNum > 9:
                                    badNums = True
                                    break
                                if (numbers[tempNum -1] == False):
                                    numbers[tempNum-1] = True
                                else:
                                    badNums = True
                    if badNums == False:
                        if (
                            grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] == 15 and # horizontal -1
                            grid[i][j - 1]     + grid[i][j]     + grid[i][j + 1]     == 15 and # horizontal
                            grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1] == 15 and # horizontal + 1
                            grid[i - 1][j - 1] + grid[i][j - 1] + grid[i + 1][j - 1] == 15 and # vertical -1
                            grid[i - 1][j]     + grid[i][j]     + grid[i + 1][j]     == 15 and # vertical
                            grid[i - 1][j + 1] + grid[i][j + 1] + grid[i + 1][j + 1] == 15 and # vertical +1
                            grid[i - 1][j - 1] + grid[i][j]     + grid[i + 1][j + 1] == 15 and # diagonal left to right
                            grid[i + 1][j - 1] + grid[i][j]     + grid[i - 1][j + 1] == 15 # diagonal right to left
                        ): 
                            retVal += 1

        return retVal
    
    

def main(): 
    thingy = Solution()
    print(thingy.numMagicSquaresInside([
    [4, 3, 8, 4],
    [9, 5, 1, 9],
    [2, 7, 6, 2]
  ]))

    assert thingy.numMagicSquaresInside([[4, 3, 8, 4],[9, 5, 1, 9],[2, 7, 6, 2]]) == 1, "Test Case 1 failed"
    
    

if __name__ == "__main__":
    main()