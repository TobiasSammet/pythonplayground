# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.

# Example 1:
# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.

# Example 2:
# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.

# Constraints:
#     1 <= k <= nums.length <= 1000
#     0 <= nums[i] <= 10^5

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        length: int = len(nums)
        if length < k:
            return 0
        retVal: int = float('inf')
        nums.sort(reverse=True)
        for i in range(0, length - k + 1):
            tempDiff: int = nums[i] - nums[i + k -1]
            retVal = min(retVal, tempDiff)
    
        return retVal

def main():
    thingy = Solution()
    assert thingy.minimumDifference([90], 1) == 0, "Test Case 1 Failed"
    assert thingy.minimumDifference([9, 4, 1, 7], 2) == 2, "Test Case 2 Failed"
    assert thingy.minimumDifference([64407, 3036], 2) == 61371, "Test Case 3 Failed"
    # assert thingy.minimumDifference() == 2, "Test Case  Failed"

if __name__ == "__main__":
    main()