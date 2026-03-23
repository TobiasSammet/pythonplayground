from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ret_val: int = 0
        length = len(grid)
        width = len(grid[0])
        pre_calc_col = [0] * width
        for i in range(length):
            row_sum: int = 0
            for j in range(width):
                pre_calc_col[j] += grid[i][j]
                row_sum += pre_calc_col[j]
                if row_sum <= k:
                    ret_val += 1

        return ret_val
    
def main():
    thingy = Solution()

    assert thingy.countSubmatrices([[7,6,3],[6,6,1]], 18) == 4, "Test Case Failed"
    assert thingy.countSubmatrices([[7,2,9],[1,5,0],[2,6,6]], 20) == 6, "Test Case Failed"
    # assert thingy.countSubmatrices() == 4, "Test Case Failed"
    # assert thingy.countSubmatrices() == 4, "Test Case Failed"

if __name__ == "__main__":
    main()