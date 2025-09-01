# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

 

# Constraints:

#     n == nums.length
#     1 <= n <= 300
#     nums[i] is either 0, 1, or 2.


from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts : List[int] = [0] * 3
        for value in nums:
            counts[value] += 1
        # print(counts)
        for i in range(0, counts[0]):
            nums[i] = 0
        for i in range(0, counts[1]):
            nums[i + counts[0]] = 1
        for i in range(0, counts[2]):
            nums[i + counts[0] + counts[1]] = 2
        # print(counts)
        

            
        



thingy = Solution()
nums: List[int] = [2,0,2,1,1,0]
nums = [2]
thingy.sortColors(nums)
print(nums)
  