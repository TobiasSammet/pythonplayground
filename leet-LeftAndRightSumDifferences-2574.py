# You are given a 0-indexed integer array nums of size n.
# Define two arrays leftSum and rightSum where:
#     leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
#     rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

# Example 1:
# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

# Example 2:
# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].

# Constraints:
#     1 <= nums.length <= 1000
#     1 <= nums[i] <= 105

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0:
            return nums
        if length == 1:
            return [0]
        
        left: int = 0
        right: int = sum(nums) - nums[0]


        ret_val: list[int] = [abs(0 - right)]
        
        for i in range(1,length):
            left += nums[i-1]
            right -= nums[i]
            ret_val.append(abs(left - right))
        
        return ret_val
    


def main():
    thingy = Solution()

    assert thingy.leftRightDifference([10,4,8,3]) == [15,1,11,22], "Test Case Failed"
    assert thingy.leftRightDifference([1]) == [0], "Test Case Failed"
    # assert thingy.leftRightDifference() == [], "Test Case Failed"
    # assert thingy.leftRightDifference() == [], "Test Case Failed"
    # assert thingy.leftRightDifference() == [], "Test Case Failed"

if __name__ == "__main__":
    main()