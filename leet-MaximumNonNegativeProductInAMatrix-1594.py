# You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.
# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.
# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.
# Notice that the modulo is performed after getting the maximum product.

# Example 1:
# Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
# Output: -1
# Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

# Example 2:
# Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
# Output: 8
# Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).

# Example 3:
# Input: grid = [[1,3],[0,-4]]
# Output: 0
# Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 15
#     -4 <= grid[i][j] <= 4
from typing import List
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        modulo: int = 1e9 + 7
        rows: int = len(grid)
        cols: int = len(grid[0])
        dp = [[(0,0) for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = (grid[0][0], grid[0][0])
        for i in range(1, cols):
            val1 = dp[0][i-1][0] * grid[0][i]
            dp[0][i] = (val1, val1)

        for i in range(1, rows):
            val1 = dp[i-1][0][0] * grid[i][0]
            dp[i][0] = (val1, val1)

        for i in range(1, rows):
            for j in range(1, cols):
                cur_val = grid[i][j]
                val1a = dp[i-1][j][0] * cur_val
                val1b = dp[i-1][j][1] * cur_val
                val2a = dp[i][j-1][0] * cur_val
                val2b = dp[i][j-1][1] * cur_val
                dp[i][j] = (min(val1a, val1b, val2a, val2b), max(val1a, val1b, val2a, val2b))

        # print(dp[rows-1][cols-1])
        ret_val = dp[rows-1][cols-1][1]
        if ret_val < 0:
            return -1
        return int(ret_val % modulo)
    

def main(): 
    thingy = Solution()
    # assert thingy.maxProductPath([[1,-2,1],[1,-2,1],[3,-4,1]]) == 8, "Test Case Failed"
    # assert thingy.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]) == -1, "Test Case Failed"
    # assert thingy.maxProductPath([[1,3],[0,-4]]) == 0, "Test Case Failed"
    assert thingy.maxProductPath([[1,4,4,0],[-2,0,0,1],[1,-1,1,1]]) == 2, "Test Case Failed"
    # assert thingy.maxProductPath() == 8, "Test Case Failed"

if __name__== "__main__":
    main()