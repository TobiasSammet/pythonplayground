# Given an array nums of n integers and an integer k, determine whether there exist two adjacent
# of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
#     Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
#     The subarrays must be adjacent, meaning b = a + k.

# Return true if it is possible to find two such subarrays, and false otherwise.

# Example 1:
# Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3
# Output: true

# Explanation:
#     The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
#     The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
#     These two subarrays are adjacent, so the result is true.

# Example 2:
# Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5
# Output: false

from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        length: int = len(nums)
        if k == 1:
            return True
        left: int = 0
        right: int = k
        currentCount: int = 1
        while right < length -1:
            if nums[left] < nums[left+1] and nums[right] < nums[right+1]:
                currentCount += 1
                if currentCount >= k:
                    return True
            else:
                currentCount = 1
            left += 1
            right += 1
        return False


def main():
    thingy = Solution()
    print(thingy.hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3)) # True
    print(thingy.hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5)) # False
    print(thingy.hasIncreasingSubarrays([5, 8, -2, -1], 2)) # True
    print(thingy.hasIncreasingSubarrays([8, 9, 13, -10, -9, -3], 3)) # True
    # print(thingy.hasIncreasingSubarrays()) # 


if __name__ == "__main__":
    main()