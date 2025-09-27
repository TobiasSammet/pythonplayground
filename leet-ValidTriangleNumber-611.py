from typing import List

# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

# Example 1:
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

# Example 2:
# Input: nums = [4,2,3,4]
# Output: 4

# Constraints:

#     1 <= nums.length <= 1000
#     0 <= nums[i] <= 1000

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length:int  = len(nums)
        if length <= 2:
            return 0
        retVal: int = 0
        for i in range(length-1, 1, -1):
            first: int = 0
            second: int = i - 1
            while first < second:
                tempSum: int = nums[first] + nums[second]
                if tempSum > nums[i]:
                    retVal += second-first
                    second -= 1
                else:
                    first += 1

        return retVal

    

def main():
    thingy = Solution()
    print(thingy.triangleNumber([2, 2, 3, 4])) # 3
    print(thingy.triangleNumber([4, 2, 3, 4])) # 4

if __name__ == "__main__":
    main()