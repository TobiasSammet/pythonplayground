# 48. Rotate Image
# Medium

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# The idea was firstly transpose the matrix and then flip it symmetrically. For instance,
# 1  2  3
# 4  5  6
# 7  8  9

# after transpose, it will be swap(matrix[i][j], matrix[j][i])
# 1  4  7
# 2  5  8
# 3  6  9

# Then flip the matrix horizontally. (swap(matrix[i][j], matrix[i][matrix.length-1-j])
# 7  4  1
# 8  5  2
# 9  6  3

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return 0
        length: int = len(matrix)
        width: int = len(matrix[0])
        
        for i in range(length):
            for j in range(i, width):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(length):
            for j in range(0, length // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][length -1 - j]
                matrix[i][length -1 - j] = temp


def main():
    thingy = Solution()
    matrix: List[List[int]] = [[1,2,3],[4,5,6],[7,8,9]]
    thingy.rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

    matrix_two: List[List[int]] = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    thingy.rotate(matrix_two)
    assert matrix_two == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


if __name__ == "__main__":
    main()