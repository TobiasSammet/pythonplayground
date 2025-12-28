# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 100
#     -100 <= grid[i][j] <= 100

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        length: int = len(grid)
        if length == 0:
            return 0
        width: int = len(grid[0])
        if width == 0:
            return 0
        retVal: int = 0

        for i in range(length-1, -1, -1):
            if grid[i][width-1] < 0:
                for j in range(width-1, -1, -1):
                    if grid[i][j] < 0:
                        retVal += 1
                    else:
                        break

        return retVal
    
def main(): 
    thingy = Solution()
    print(thingy.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # 8
    print(thingy.countNegatives([[3,2],[1,0]])) # 0
    
    assert thingy.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]) == 8, "Test Case 1 failed"
    assert thingy.countNegatives([[3,2],[1,0]]) == 0, "Test Case 2 failed"
    

if __name__ == "__main__":
    main()