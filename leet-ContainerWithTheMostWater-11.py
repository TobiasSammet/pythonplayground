# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
#     n == height.length
#     2 <= n <= 105
#     0 <= height[i] <= 104

# I am Using two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length: int = len(height)
        if length <= 1:
            return 0
        retVal: int = 0
        left: int = 0
        right: int = length -1
        while left < right:
            leftHeight: int = height[left]
            rightHeight: int = height[right]
            theHeight: int = min(leftHeight, rightHeight)
            area: int = theHeight * (right - left)
            retVal = max(retVal, area)
            if leftHeight < rightHeight:
                left += 1
            else:
                right -= 1
        return retVal
    

def main(): 
    thingy = Solution()
    print(thingy.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49
    print(thingy.maxArea([1, 1])) # 1
    print(thingy.maxArea([1, 0, 0, 0, 0, 0, 0, 2, 2])) # 8
    # print(thingy.maxArea()) #
    

if __name__ == "__main__":
    main()
