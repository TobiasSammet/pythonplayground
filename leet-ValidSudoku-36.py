from typing import List
import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: List[List[bool]] = [ [False]*9 for _ in range(9) ]    
        cols: List[List[bool]] = [ [False]*9 for _ in range(9) ]    
        boxes: List[List[bool]] = [ [False]*9 for _ in range(9) ]   
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != ".":
                    temp: int = int(board[i][j]) -1
                    boxIndex: int = math.floor(i/3) * 3 + math.floor(j/3)
                    if rows[i][temp] or cols[j][temp] or boxes[boxIndex][temp]:
                        return False
                    rows[i][temp] = cols[j][temp] = boxes[boxIndex][temp] = True

        return True


def main():
    thingy = Solution()
    # True
    print(thingy.isValidSudoku([
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]))
    # False
    print(thingy.isValidSudoku([
        ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]))

if __name__ == "__main__":
    main()