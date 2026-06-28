# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].

# Example 2:
# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.

# Example 3:
# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

# Constraints:
#     1 <= nums.length <= 100
#     1 <= nums[i] <= 100

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        length: int = len(nums)
        found_start_index: bool = False
        start_index: int = 0

        for i in range(length-1):
            if nums[i] > nums[i+1]:
                found_start_index = True
                start_index = i + 1
                break

        if found_start_index == False:
            return True
        
        for i in range(length-1):
            if nums[(i + start_index) % length] > nums[(i + 1 + start_index) % length]:
                return False
        
        return True

def main():
    thingy = Solution()
    assert thingy.check(nums = [3,4,5,1,2]) ==True, "Test Case Failed"
    assert thingy.check(nums = [2,1,3,4]) ==False, "Test Case Failed"
    assert thingy.check(nums = [1,2,3]) ==True, "Test Case Failed"
    assert thingy.check(nums = [1,1,1]) ==True, "Test Case Failed"
    # assert thingy.check() ==True, "Test Case Failed"



if __name__ == "__main__":
    main()