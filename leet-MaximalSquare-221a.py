from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        retVal: int = 0
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        if rows == 0:
            return 0
        if cols == 0: 
            return 0
        # declare and prefill 2 dimension "array"
        dp: List[List[int]] = [ [0]*cols for _ in range(rows) ]
        
        for i in range(0, cols):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                retVal = 1
        for i in range(0, rows):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                retVal = 1
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    retVal = max(retVal, dp[i][j])



        return retVal * retVal


thing = Solution()    
# matrix: List[List[str]] = [
#     ["1", "1"],
#     ["1", "1"]
# ]
matrix: List[List[str]] = [
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0'],
]

print(thing.maximalSquare(matrix))