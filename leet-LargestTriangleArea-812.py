# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.

# Example 2:
# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000

# Constraints:
#     3 <= points.length <= 50
#     -50 <= xi, yi <= 50
#     All the given points are unique.


from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        retVal: int = 0
        length: int = len(points)

        for i in range(0, length):
            for j in range(1, length):
                if i != j :
                    for k in range(2, length):
                        if i !=k and j != k:
                            retVal = max(retVal, self.__calcAreaOfTriangle(points[i], points[j], points[k]))
        return retVal
    
    def __calcAreaOfTriangle(self, a: List[int], b: List[int], c: List[int]) -> float:
        numerator = abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
        return numerator / 2
    

def main() :
    thingy = Solution()

    print(thingy.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])) # 2
    print(thingy.largestTriangleArea([[1,0],[0,0],[0,1]])) # 0.5
    
    # print(thingy.largestTriangleArea([]))


if __name__ == "__main__": 
    main()