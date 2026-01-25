# Given an array nums, you can perform the following operation any number of times:
#     Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
#     Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.
# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

# Example 1:
# Input: nums = [5,2,3,1]
# Output: 2
# Explanation:
#     The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
#     The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

# Example 2:
# Input: nums = [1,2,2]
# Output: 0
# Explanation:
# The array nums is already sorted.

# Constraints:
#     1 <= nums.length <= 50
#     -1000 <= nums[i] <= 1000

from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        retVal: int = 0
        while len(nums) > 1:
            isAscending: bool = True
            minSumIndex: int = -1
            minSum: int = float('inf')
            for i in range(0, len(nums)-1):
                tempSum: int = nums[i] + nums[i+1]
                if nums[i] > nums[i+1]:
                    isAscending = False
                if tempSum < minSum:
                    minSum = tempSum
                    minSumIndex = i
            if isAscending:
                return retVal
            nums[minSumIndex] = minSum
            nums.pop(minSumIndex + 1)
            retVal += 1
            
        return retVal


    


def main():
    thingy = Solution()
    assert thingy.minimumPairRemoval([5, 2, 3, 1]) == 2, "Test Case 1 Failed"
    # assert thingy.minimumPairRemoval([1,2,2]) == 0, "Test Case 2 Failed"
    # assert thingy.minimumPairRemoval() == 1, "Test Case Failed"

if __name__ == "__main__":
    main()