from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left : int = 1001
        right: int = -1
        top = 1001
        bottom: int = -1
        rows = len(grid)
        cols = len(grid[0])
        if (rows == 0) or (cols == 0):
            return 0
        if (rows == 1) and (cols == 1):
            return 1
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    bottom = max(bottom, i)

        # if cols == 1:
        #     return abs(top - bottom) + 1
        # if rows == 1:
        #     return abs(left - right) + 1
        return (bottom - top + 1) * (right - left + 1)
    


thingy = Solution()

print(thingy.minimumArea([
    [0, 1, 0],
    [1, 0, 1],
  ])) # 6
print(thingy.minimumArea([
    [1, 0],
    [0, 0],
  ])) # 1
print(thingy.minimumArea([[0], [1]])) # 1
print(thingy.minimumArea([[1]])) # 1
print(thingy.minimumArea([[0, 1]])) # 1
# print(thingy.minimumArea([]))
# print(thingy.minimumArea([]))