# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.
# The following proccess happens k times:
#     Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
#     Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
# Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4
# Output: false
# Explanation:
# In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).

# Example 2:
# Input: mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2
# Output: true
# Explanation:

# Example 3:
# Input: mat = [[2,2],[2,2]], k = 3
# Output: true
# Explanation:
# As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.

# Constraints:
#     1 <= mat.length <= 25
#     1 <= mat[i].length <= 25
#     1 <= mat[i][j] <= 25
#     1 <= k <= 50

from typing import List

class Solution:
    def xareSimilar(self, mat: List[List[int]], k: int) -> bool:
        copied_array = [row[:] for row in mat]
        rows: int = len(mat)
        cols: int = len(mat[0])

        for i in range(k):
            for row in range(rows):
                if row % 2 == 0:
                    # shift to left
                    tempVal = mat[row][0]
                    for col in range(cols-1):
                        mat[row][col] = mat[row][col+1]
                    mat[row][cols -1] = tempVal
                else:
                    tempVal = mat[row][cols-1]
                    for col in range(cols-1, 0, -1):
                        mat[row][col] = mat[row][col-1]
                    mat[row][0] = tempVal
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != copied_array[i][j]:
                    return False
        return True
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows: int = len(mat)
        cols: int = len(mat[0])
        for j in range(cols):
            forward_column: int = (j + k) % cols
            backward_column: int = (((j - k) % cols) + cols) % cols
            for i in range(rows):
                if i % 2 == 0:
                    if mat[i][j] != mat[i][forward_column]:
                        return False
                else:
                    if mat[i][j] != mat[i][backward_column]:
                        return False
        return True

def main():
    thingy = Solution()
    assert thingy.areSimilar( mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4) == False, "Test Case Failed"
    assert thingy.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2) == True, "Test Case Failed"
    assert thingy.areSimilar(mat = [[2,2],[2,2]], k = 3) == True, "Test Case Failed"
    # assert thingy.areSimilar() == False, "Test Case Failed"

if __name__ == "__main__":
    main()
