# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
# To separate the digits of an integer is to get all the digits it has in the same order.
#     For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

# Example 1:
# Input: nums = [13,25,83,77]
# Output: [1,3,2,5,8,3,7,7]
# Explanation:
# - The separation of 13 is [1,3].
# - The separation of 25 is [2,5].
# - The separation of 83 is [8,3].
# - The separation of 77 is [7,7].
# answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

# Example 2:
# Input: nums = [7,1,3,9]
# Output: [7,1,3,9]
# Explanation: The separation of each integer in nums is itself.
# answer = [7,1,3,9].

# Constraints:
#     1 <= nums.length <= 1000
#     1 <= nums[i] <= 105

from typing import List 

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret_val: List[int] = []
        for num in nums:
            tempVal: str = str(num)
            for char in tempVal:
                ret_val.append(int(char))
        return ret_val

    

def main():
    thingy = Solution()
    assert thingy.separateDigits(nums = [13,25,83,77]) == [1,3,2,5,8,3,7,7], "Test Case Failed"
    assert thingy.separateDigits(nums = [7,1,3,9]) == [7,1,3,9], "Test Case Failed"
    # assert thingy.separateDigits() == , "Test Case Failed"

if __name__ == "__main__":
    main()