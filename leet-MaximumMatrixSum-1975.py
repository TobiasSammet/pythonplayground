# You are given an n x n integer matrix. You can do the following operation any number of times:
#     Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

# Example 1:
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.

# Example 2:
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.

# Constraints:
#     n == matrix.length == matrix[i].length
#     2 <= n <= 250
#     -105 <= matrix[i][j] <= 105
from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        length: int = len(matrix)
        if length == 0:
            return 0
        width: int = len(matrix[0])
        if width == 0:
            return 0
        retVal: int = 0
        smallest: int = abs(matrix[0][0])
        negativeCount: int = 0

        for i in range(0, length):
            for j in range(0, width):
                tempVal = matrix[i][j]
                if tempVal < 0:
                    negativeCount += 1
                retVal += abs(tempVal)
                smallest = min(smallest, abs(tempVal))

        # if there are an odd amount of negatives we cannot flip them all to positive 
        # so we have to substract the smallest number from the total. However since 
        # we've already added it to the total we have to subtract it twice
        if negativeCount % 2 == 1:
            retVal -= (2 * smallest)
        return retVal

    

def main():
    thing = Solution()
    print(thing.maxMatrixSum([[1,-1],[-1,1]])) # 4
    print(thing.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])) # 16
    # print(thing.maxMatrixSum()) # 
    
    assert thing.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]) == 16, "Test Case Failed"


if __name__ == "__main__":
    main()   