# You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.
# You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.
# Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

# Example 1:
# Input: n = 2, m = 1, hBars = [2,3], vBars = [2]
# Output: 4
# Explanation:
# The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4], and the vertical bars are [1,2,3].
# One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

# Example 2:
# Input: n = 1, m = 1, hBars = [2], vBars = [2]
# Output: 4
# Explanation:
# To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.

# Example 3:
# Input: n = 2, m = 3, hBars = [2,3], vBars = [2,4]
# Output: 4
# Explanation:
# One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.

# Constraints:
#     1 <= n <= 109
#     1 <= m <= 109
#     1 <= hBars.length <= 100
#     2 <= hBars[i] <= n + 1
#     1 <= vBars.length <= 100
#     2 <= vBars[i] <= m + 1
#     All values in hBars are distinct.
#     All values in vBars are distinct.

# figure out the biggest gap for the vertivcal and horizontal and take the smaller of the 2 and square it


from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        verticalGap: int = self._getBiggestGap(vBars)
        horizontalGap: int = self._getBiggestGap(hBars)

        side: int = min(verticalGap, horizontalGap)

        return side ** 2
    
    def _getBiggestGap(self,bars: List[int]) -> int:
        if len(bars) == 0:
            return 1
        bars.sort()
        currentLength: int = 2
        retVal: int = 2
        for i in range(1, len(bars)):
            if bars[i] == bars[i-1] + 1:
                currentLength += 1
            else: 
                currentLength = 2
            retVal = max(retVal, currentLength)
        return retVal



def main() : 
    thingy = Solution()
    print(thingy.maximizeSquareHoleArea(1, 5, [2], [2,3])) # 4
    # assert thingy.maximizeSquareHoleArea(2, 1, [2, 3], [2]) == 4, "Test case 1 failed"
    # assert thingy.maximizeSquareHoleArea(1, 1, [2], [2]) == 4, "Test case 2 failed"
    # assert thingy.maximizeSquareHoleArea(2, 3, [2, 3], [2,4]) == 4, "Test case 3 failed"
    
    # assert thingy.maximizeSquareHoleArea(4,40,[5,3,2,4],[36,41,6,34,33]) == 9, "Test case 4 failed"


if __name__ == "__main__":
    main()