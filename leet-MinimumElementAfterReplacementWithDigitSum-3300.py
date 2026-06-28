# You are given an integer array nums.
# You replace each element in nums with the sum of its digits.
# Return the minimum element in nums after all replacements.

# Example 1:
# Input: nums = [10,12,13,14]
# Output: 1
# Explanation:
# nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation:
# nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

# Example 3:
# Input: nums = [999,19,199]
# Output: 10
# Explanation:
# nums becomes [27, 10, 19] after all replacements, with minimum element 10.

# Constraints:
#     1 <= nums.length <= 100
#     1 <= nums[i] <= 10^4


from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        newVals : List[int]  = []

        for num in nums:
            tempVal: int = 0
            while num > 0:
                tempVal += num % 10
                num = num // 10
            newVals.append(tempVal)

        return min(newVals)
    

def main(): 
    thingy = Solution()

    assert thingy.minElement([10, 12, 13, 14]) == 1, "Test Case Failed"
    assert thingy.minElement([1, 2, 3, 4]) == 1, "Test Case Failed"
    assert thingy.minElement([999, 19, 199]) == 10, "Test Case Failed"
    # assert thingy.minElement() == 0, "Test Case Failed"


if __name__ == "__main__":
    main()