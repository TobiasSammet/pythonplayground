from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        retVal: int = 0
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        if rows == 0:
            return 0
        if cols == 0: 
            return 0
        # declare and prefill 2 dimension "array"
        dp: List[List[int]] = [ [0]*cols for _ in range(rows) ]    


        # run down the first row
        for j in range(0, cols):
            if matrix[0][j] == "1":
                dp[0][j] = 1

        # run down the rest of the rows
        for i in range(1, rows):
            for j in range(0, cols):
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i-1][j] + 1

        # print(dp)
        for i in range(0, rows):
            for j in range(0, cols):
                if dp[i][j] != 0:
                    currentHeight: int = dp[i][j]
                    currentWidth: int = 1
                    # print("calc retVal")
                    retVal = max(retVal, currentHeight * currentWidth)
                    currentColumn: int = j-1
                    while currentColumn >= 0:
                        if dp[i][currentColumn] == 0:
                            break
                        currentHeight = min(currentHeight, dp[i][currentColumn])
                        currentWidth += 1
                        retVal = max(retVal, currentHeight * currentWidth)
                        currentColumn -= 1
        return retVal

thingy = Solution()

# print(thingy.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 6
print(thingy.maximalRectangle([["0","1"]])) # 1