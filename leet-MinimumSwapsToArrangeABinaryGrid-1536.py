from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        length: int = len(grid)
        max_right: List[int] = [-1] * length
        ret_val: int = 0
        for i in range(length):
            for j in range(length-1, -1, -1):
                if grid[i][j] == 1:
                    max_right[i] = j
                    break

        # Check if solution is possible
        max_right_sorted = max_right.copy()
        max_right_sorted.sort()
        for i in range(length):
            if max_right_sorted[i] > i:
                return -1
        
        # Greedy approach: for each row, find the first valid row and move it up
        for i in range(length):
            # Find the first row that can go in position i (maxRight[j] <= i)
            target_row: int = -1
            for j in range(i, length):
                if max_right[j] <= i:
                    target_row = j
                    break
            if target_row == -1: # Should not happen if solution exists
                return -1
            
            while target_row > i:
                temp: int= max_right[target_row]
                max_right[target_row] = max_right[target_row -1]
                max_right[target_row -1] = temp
                target_row -= 1
                ret_val += 1
        print(ret_val)
        return ret_val
    

def main():
    thingy = Solution()
    assert thingy.minSwaps([[0,0,1],[1,1,0],[1,0,0]]) == 3, "Test Case Failed"
    assert thingy.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]) == -1, "Test Case Failed"
    assert thingy.minSwaps([[1,0,0],[1,1,0],[1,1,1]]) == 0, "Test Case Failed"
    # assert thingy.minSwaps([]) == 1, "Test Case Failed"
    # assert thingy.minSwaps([]) == 1, "Test Case Failed"


if __name__ == "__main__":
    main()