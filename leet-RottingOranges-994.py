from typing import List
import copy

class Solution:

    ROTTEN: int = 2
    FRESH: int = 1
    EMPTY: int = 0

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        if self.allRotten(grid):
            return 0
        if self.allEmpty(grid):
            return 0
        if self.noRotten(grid):
            return -1
        for i in range(len(grid) * 2 + 1):
            grid = self.calcNextGeneration(grid)
            if self.allRotten(grid):
                return i + 1
        
        return -1

    def calcNextGeneration(self, world: List[List[int]]) -> List[List[int]]:
        retVal: List[List[int]] = copy.deepcopy(world)
        for i in range(len(world)):
            for j in range(len(world[i])):
                if world[i][j] == self.FRESH:
                    if self.willBeRotten(world, i, j):
                        retVal[i][j] = self.ROTTEN
                    else :
                        retVal[i][j] = self.FRESH
        return retVal

    def willBeRotten(self, grid: List[List[int]], i: int, j: int):
        if i != 0:
            if grid[i-1][j] == self.ROTTEN:
                return True

        if i != len(grid) -1:
            if grid[i+1][j] == self.ROTTEN:
                return True

        if j != 0:
            if grid[i][j-1] == self.ROTTEN:
                return True

        if j != len(grid[i]) -1 :
            if grid[i][j+1] == self.ROTTEN:
                return True
        return False

    def allRotten(self, grid: List[List[int]]) -> bool:
        for row in grid:
            for col in row:
                if col == self.FRESH:
                    return False
        return True

    def noRotten(self, grid: List[List[int]]) -> bool:
        for row in grid:
            for col in row:
                if col == self.ROTTEN:
                    return False
        return True

    def allEmpty(self, grid: List[List[int]]) -> bool:
        for row in grid:
            for col in row:
                if col != self.EMPTY:
                    return False
        return True



thing = Solution()

grid: List[List[int]] = [[2,1,1], [1,1,0], [0,1,1]]

print(thing.orangesRotting(grid))