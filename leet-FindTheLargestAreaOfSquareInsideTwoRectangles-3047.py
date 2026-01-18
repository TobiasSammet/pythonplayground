# There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.
# You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.

# Example 1:
# Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
# Output: 1
# Explanation:
# A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

# Example 2:
# Input: bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]
# Output: 4
# Explanation:
# A square with side length 2 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 2 * 2 = 4. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

# Example 3:
# Input: bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]
# Output: 1
# Explanation:
# A square with side length 1 can fit inside the intersecting region of any two rectangles. Also, no larger square can, so the maximum area is 1. Note that the region can be formed by the intersection of more than 2 rectangles.

# Example 4:
# Input: bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]
# Output: 0
# Explanation:
# No pair of rectangles intersect, hence, the answer is 0.

# Constraints:
#     n == bottomLeft.length == topRight.length
#     2 <= n <= 103
#     bottomLeft[i].length == topRight[i].length == 2
#     1 <= bottomLeft[i][0], bottomLeft[i][1] <= 107
#     1 <= topRight[i][0], topRight[i][1] <= 107
#     bottomLeft[i][0] < topRight[i][0]
#     bottomLeft[i][1] < topRight[i][1]

# Brutal - just brutal

from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        length: int = len(bottomLeft)
        if length <= 1:
            return 0
        retVal: int = 0
        for i in range(0, length-1):
            for j in range(i+1, length):
                bl1 = bottomLeft[i]
                tr1 = topRight[i]
                bl2 = bottomLeft[j]
                tr2 = topRight[j]
                #  Two rectangles will not overlap when the bottom left x coordinate of one rectangle is greater than the top right x coordinate of the other rectangle.
                #    The same is true for the y coordinate.
                if (bl1[0] <= tr2[0]) and (bl1[1] <= tr2[1]):
                    minX = max(bl1[0], bl2[0])
                    maxX = min(tr1[0], tr2[0])
                    minY = max(bl1[1], bl2[1])
                    maxY = min(tr1[1], tr2[1])
                    tempLen = min(maxX - minX, maxY - minY)
                    retVal = max(retVal, tempLen)
      
        return retVal * retVal
    

def main(): 
    thingy = Solution()
    assert thingy.largestSquareArea([[1,1],[2,2],[3,1]], [[3,3],[4,4],[6,6]]) == 1, "Test Case 1 Failed"
    assert thingy.largestSquareArea([[1,1],[1,3],[1,5]], [[5,5],[5,7],[5,9]]) == 4, "Test Case 2 Failed"
    assert thingy.largestSquareArea([[1,1],[2,2],[1,2]], [[3,3],[4,4],[3,4]]) == 1, "Test Case 3 Failed"
    assert thingy.largestSquareArea([[1,1],[3,3],[3,1]], [[2,2],[4,4],[4,2]]) == 0, "Test Case 4 Failed"
    # assert thingy.largestSquareArea() == 4, "Test Case X Failed"
    


if __name__ == "__main__":
    main()    