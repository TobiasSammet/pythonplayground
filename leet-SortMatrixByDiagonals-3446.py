from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        size: int = len(grid)
        if size <= 1:
            return grid
        retVal: List[List[int]] = [ [0]*size for _ in range(size) ]

        # first we fill in based on cols
        for i in range(0, size):
            temp: list[int] = []
            currentX: int = i
            currentY: int = 0
            while currentX < size:
                temp.append(grid[currentX][currentY])
                currentX += 1
                currentY += 1
            temp.sort(reverse=True)
            # print(temp)

            currentX = i
            currentY = 0
            while currentX < size:
                retVal[currentX][currentY] = temp[currentY]
                currentX += 1
                currentY += 1

        # next do the rows
        for i in range(1, size):
            temp: list[int] = []
            currentX: int = 0
            currentY: int = i
            while currentY < size:
                temp.append(grid[currentX][currentY])
                currentX += 1
                currentY += 1
            temp.sort()
            # print(temp)

            currentX = 0
            currentY = i
            while currentY < size:
                retVal[currentX][currentY] = temp[currentX]
                currentX += 1
                currentY += 1

        return retVal
    
def main():
    thingy = Solution()
    # [[8,2,3],[9,6,7],[4,5,1]]
    print(thingy.sortMatrix([[1,7,3],[9,8,2],[4,5,6]]))
    # [[2,1],[1,0]]
    print(thingy.sortMatrix([[0,1],[1,2]]))
    # [[1]]
    # print(thingy.sortMatrix([[1]]))

if __name__ == "__main__":
    main()