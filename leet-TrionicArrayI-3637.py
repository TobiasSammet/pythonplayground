# You are given an integer array nums of length n.
# An array is trionic if there exist indices 0 < p < q < n − 1 such that:
#     nums[0...p] is strictly increasing,
#     nums[p...q] is strictly decreasing,
#     nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.

# Example 1:
# Input: nums = [1,3,5,4,2,6]
# Output: true

# Explanation:
# Pick p = 2, q = 4:
#     nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
#     nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
#     nums[4...5] = [2, 6] is strictly increasing (2 < 6).

# Example 2:
# Input: nums = [2,1,3]
# Output: false

# Explanation:
# There is no way to pick p and q to form the required three segments.

# Constraints:
#     3 <= n <= 100
#     -1000 <= nums[i] <= 1000

from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        length: int = len(nums)
        peak: int = 0
        valley: int = 0

        # make sure there are no plains (same number twice in a row)
        for i in range(0, length -1):
            if nums[i] == nums[i+1]:
                return False

        # find first peak
        for i in range(0, length -1):
            if nums[i] > nums[i+1]:
                peak = i
                break
        if peak == 0:
            return False
        # find the last valley
        for i in range(length-2, 0, -1):
            if nums[i] > nums[i+1]:
                valley = i + 1
                break
        if (valley == 0) or (valley == length -1) or (peak > valley):
            return False
    
        # make sure everything between peak and valley is decending
        for i in range(peak, valley-1):
            if nums[i] < nums[i+1]:
                return False
        return True

def main():
    thingy = Solution()
    # assert thingy.isTrionic([1, 3, 5, 4, 2, 6]) == True, "Test case failed"
    # assert thingy.isTrionic([2, 1, 3]) == False, "Test case failed"
    # assert thingy.isTrionic([5, 6, 9, 3, 7]) == True, "Test case failed"
    # assert thingy.isTrionic([8, 9, 4, 6, 1]) == False, "Test case failed"
    assert thingy.isTrionic([6,7,5,1]) == False, "Test case failed"
    # assert thingy.isTrionic([1,2,2,3]) == False, "Test case failed"

if __name__ == "__main__":
    main()