# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return 
        todo_list: List[int, int] = []
        column_count = len(matrix[0])

        for i in range(0, len(matrix)):
            for j in range(0, column_count):
                if matrix[i][j] == 0:
                    todo_list.append([i,j])

        for item in todo_list:
            row = item[0]
            col = item[1]
            for i in range(0, len(matrix)):
                matrix[i][col] = 0
            for j in range(0, column_count):
                matrix[row][j] = 0
        return


matrix = [[1,1,1],[1,0,1],[1,1,1]]
thingy = Solution()

thingy.setZeroes(matrix)

print(matrix)

