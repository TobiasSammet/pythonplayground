from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # no flips necessary
        if k == 1:
            return grid
        
        for i in range(k//2):
            for j in range(k):
                temp = grid[i +x][j + y]
                grid[i +x][j + y] = grid[x + k - i - 1][j + y]
                grid[x + k - i - 1][j + y] = temp

        return grid
    

def main():
    thingy = Solution()
    assert thingy.reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3) == [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]], "Test Case Failed"
    assert thingy.reverseSubmatrix([[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2) == [[3,4,4,2],[2,3,2,3]], "Test Case Failed"
    # assert thingy.reverseSubmatrix() == , "Test Case Failed"
    # assert thingy.reverseSubmatrix() == , "Test Case Failed"

if __name__ == "__main__":
    main()