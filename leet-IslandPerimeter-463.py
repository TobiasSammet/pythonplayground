from typing import List

class Solution :
    def islandPerimeter(self, g: List[List[int]]) -> int :
        retVal: int = 0
        height: int = len(grid)
        width: int = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        retVal +=1
                    if j == 0 or grid[i][j-1] == 0:
                        retVal +=1
                    if i == height -1 or grid[i+1][j] == 0:
                        retVal += 1
                    if j == width -1 or grid[i][j+1] == 0:
                        retVal +=1
        return retVal

thing = Solution()
grid: List[List[int]] = [  [0, 1, 0, 0], [1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(thing.islandPerimeter(grid))