# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of that contain:
#     grid[0][0]
#     an equal frequency of 'X' and 'Y'.
#     at least one 'X'.

# Example 1:
# Input: grid = [["X","Y","."],["Y",".","."]]
# Output: 3

# Example 2:
# Input: grid = [["X","X"],["X","Y"]]
# Output: 0

# Explanation:
# No submatrix has an equal frequency of 'X' and 'Y'.

# Example 3:
# Input: grid = [[".","."],[".","."]]
# Output: 0
# Explanation:
# No submatrix has at least one 'X'.

# Constraints:
#     1 <= grid.length, grid[i].length <= 1000
#     grid[i][j] is either 'X', 'Y', or '.'.

from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ret_val: int = 0
        length = len(grid)
        width = len(grid[0])
        pre_calc_col = [0] * width
        x_in_col = [False] * width
        for i in range(length):
            row_sum: int = 0
            for j in range(width):
                temp_val: str = grid[i][j]
                if temp_val == "X":
                    pre_calc_col[j] += 1
                    x_in_col[j] = True
                if temp_val == "Y":
                    pre_calc_col[j] -= 1
                if x_in_col[j] == False and j > 0:
                    x_in_col[j] = x_in_col[j-1]                    
                                
                row_sum += pre_calc_col[j]
                if row_sum == 0 and x_in_col[j] == True:
                    ret_val += 1

        return ret_val
def main():
    thingy = Solution()
    # assert thingy.numberOfSubmatrices([["X","Y","."],["Y",".","."]]) == 3, "Test Case Failed"
    # assert thingy.numberOfSubmatrices([["X","X"],["X","Y"]]) == 0, "Test Case Failed"
    # assert thingy.numberOfSubmatrices([[".","."],[".","."]]) == 0, "Test Case Failed"
    assert thingy.numberOfSubmatrices([[".","X"],[".","Y"]]) == 1, "Test Case Failed"

if __name__ == "__main__":
    main()