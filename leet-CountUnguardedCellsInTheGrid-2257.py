# You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
# A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
# Return the number of unoccupied cells that are not guarded.

# Example 1:
# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
# Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
# There are a total of 7 unguarded cells, so we return 7.

# Example 2:
# Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
# Output: 4
# Explanation: The unguarded cells are shown in green in the above diagram.
# There are a total of 4 unguarded cells, so we return 4.

# Constraints:
#     1 <= m, n <= 105
#     2 <= m * n <= 105
#     1 <= guards.length, walls.length <= 5 * 104
#     2 <= guards.length + walls.length <= m * n
#     guards[i].length == walls[j].length == 2
#     0 <= rowi, rowj < m
#     0 <= coli, colj < n
#     All the positions in guards and walls are unique.

from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
         # declare and prefill 2 dimension "array"
        #  dp: List[List[int]] = [ [0]*cols for _ in range(rows) ]
        grid: List[List[str]] = [ [" "]*n for _ in range(m) ]

        # place the walls
        for wall in walls:
            grid[wall[0]][wall[1]] = "W"

        # place the guards
        for guard in guards:
            grid[guard[0]][guard[1]] = "G"

        # now check the directions
        for guard in guards:
            
            # north
            temp: int = guard[0] -1
            while temp >= 0:
                cellValue: str = grid[temp][guard[1]]
                if cellValue == " " or cellValue == "X":
                    grid[temp][guard[1]] = "X"
                    temp -= 1
                else:
                    break
            # south
            temp = guard[0] + 1
            while temp < m:
                cellValue: str = grid[temp][guard[1]]
                if cellValue == " " or cellValue == "X":
                    grid[temp][guard[1]] = "X"
                    temp += 1
                else:
                    break
            # west
            temp = guard[1] -1
            while temp >= 0:
                cellValue: str = grid[guard[0]][temp]
                if cellValue == " " or cellValue == "X":
                    grid[guard[0]][temp] = "X"
                    temp -= 1
                else:
                    break
            # east
            temp = guard[1] + 1
            while temp < n:
                cellValue: str = grid[guard[0]][temp]
                if cellValue == " " or cellValue == "X":
                    grid[guard[0]][temp] = "X"
                    temp += 1
                else:
                    break
        retVal: int = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == " ": 
                    retVal += 1

        return retVal 
    

def main(): 
    thingy = Solution()

    print(thingy.countUnguarded(4,6,[[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]])) # 7
    # print(thingy.countUnguarded(3,3,[[1,1]], [[0,1],[1,0]])) # 4
    # print(thingy.countUnguarded()) # 
    # print(thingy.countUnguarded()) # 
    
if __name__ == "__main__":
    main()    