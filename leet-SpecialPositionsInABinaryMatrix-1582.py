# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

# Example 1:
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

# Example 2:
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

# Constraints:

#     m == mat.length
#     n == mat[i].length
#     1 <= m, n <= 100
#     mat[i][j] is either 0 or 1.

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows: int = len(mat)
        cols: int = len(mat[0])
        if rows == 0 or cols == 0:
            return 0
        ret_val: int = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    only_one: bool = True
                    # check the row
                    for temp in range(cols):
                        if mat[i][temp] == 1 and temp != j:
                            only_one = False
                            break
                    #check the column
                    if only_one:
                        for temp in range(rows):
                            if mat[temp][j] == 1 and temp != i:
                                only_one = False
                                break
                    if only_one:
                        ret_val += 1
        return ret_val
                


def main():
    thingy = Solution()
    assert thingy.numSpecial([[1,0,0],[0,0,1],[1,0,0]]) == 1, "Test case failed"
    assert thingy.numSpecial([[1,0,0],[0,1,0],[0,0,1]]) == 3, "Test case failed"
    # assert thingy.numSpecial() == 0, "Test case failed"
    # assert thingy.numSpecial() == 0, "Test case failed"
    



if __name__ == "__main__":
    main()      