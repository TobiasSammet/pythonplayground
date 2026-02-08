# You are given an integer array nums and an integer k.
# An array is considered balanced if the value of its maximum element is at most k times the minimum element.
# You may remove any number of elements from nums​​​​​​​ without making it empty.
# Return the minimum number of elements to remove so that the remaining array is balanced.
# Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

# Example 1:
# Input: nums = [2,1,5], k = 2
# Output: 1

# Explanation:
#     Remove nums[2] = 5 to get nums = [2, 1].
#     Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.

# Example 2:
# Input: nums = [1,6,2,9], k = 3

# Output: 2
# Explanation:
#     Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
#     Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.

# Example 3:
# Input: nums = [4,6], k = 2
# Output: 0

# Explanation:
#     Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.

# Constraints:
#     1 <= nums.length <= 10^5
#     1 <= nums[i] <= 10^9
#     1 <= k <= 10^5

from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        length: int = len(nums)
        if length <= 1:
            return 0
        left: int = 0
        right: int = 0
        retVal: int = float('inf')

        while right < length:
            if nums[left] * k >= nums[right]:
                tempVal: int = length - (right -left + 1)
                retVal = min(retVal, tempVal)
                right += 1
            else:
                left += 1
        return retVal
    
def main():
    thingy = Solution()
    assert thingy.minRemoval([2, 1, 5], 2) == 1, "Test Case failed"
    assert thingy.minRemoval([1, 6, 2, 9], 3) == 2, "Test Case failed"
    assert thingy.minRemoval([4, 6], 2) == 0, "Test Case failed"
    assert thingy.minRemoval([1, 34, 23], 2) == 1, "Test Case failed"
    assert thingy.minRemoval([51, 70, 9, 21], 2) == 2, "Test Case failed"
    assert thingy.minRemoval([2, 12], 2) == 1, "Test Case failed"
    # assert thingy.minRemoval() == 0, "Test Case failed"
    

if __name__ == "__main__":
    main()
