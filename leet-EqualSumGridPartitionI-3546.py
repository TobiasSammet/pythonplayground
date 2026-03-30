# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
#     Each of the two resulting sections formed by the cut is non-empty.
#     The sum of the elements in both sections is equal.
# Return true if such a partition exists; otherwise return false.

# Example 1:
# Input: grid = [[1,4],[2,3]]
# Output: true
# Explanation:
# A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

# Example 2:
# Input: grid = [[1,3],[2,4]]
# Output: false
# Explanation:
# No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

# Constraints:
#     1 <= m == grid.length <= 10^5
#     1 <= n == grid[i].length <= 10^5
#     2 <= m * n <= 10^5
#     1 <= grid[i][j] <= 10^5
from typing import List
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows: int = len(grid)
        cols: int = len(grid[0])
        rowValues: List[int] = []

        tempVal: int = 0
        for i in range(rows):
            for j in range(cols):
                tempVal += grid[i][j]
            rowValues.append(tempVal)

        if tempVal % 2 == 1:
            return False
        
        testVal: int = tempVal / 2

        for i in range(rows):
            if rowValues[i] == testVal:
                return True
            if rowValues[i] > testVal:
                break

        tempVal = 0
        for j in range(cols):
            for i in range(rows):
                tempVal += grid[i][j]
            if tempVal == testVal:
                return True
            if tempVal > testVal:
                return False

        return False
    

def main():
    thingy = Solution()
    assert thingy.canPartitionGrid([[1,4],[2,3]]) == True, "Test Case Failed"
    assert thingy.canPartitionGrid([[1,3],[2,4]]) == False, "Test Case Failed"
    # assert thingy.canPartitionGrid() == True, "Test Case Failed"

if __name__ == "__main__":
    main()

