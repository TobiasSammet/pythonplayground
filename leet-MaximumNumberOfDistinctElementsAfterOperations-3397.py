# You are given an integer array nums and an integer k.
# You are allowed to perform the following operation on each element of the array at most once:
#     Add an integer in the range [-k, k] to the element.
# Return the maximum possible number of distinct elements in nums after performing the operations.

# Example 1:
# Input: nums = [1,2,2,3,3,4], k = 2
# Output: 6
# Explanation:
# nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

# Example 2:
# Input: nums = [4,4,4,4], k = 1
# Output: 3
# Explanation:
# By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

# Constraints:
#     1 <= nums.length <= 105
#     1 <= nums[i] <= 109
#     0 <= k <= 109

from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if k >= len(nums):
            return len(nums)
        
        nums.sort()

        retVal: int = 0
        # keep track of the smallest number we can use
        min: int = float('-inf')

        for num in nums:
            # if there is a number in the range we can use
            if min < num + k:
                retVal += 1
                min = max(num -k, min+1)


        return retVal
    

def main():
    thingy = Solution()
    print(thingy.maxDistinctElements([1, 2, 2, 3, 3, 4], 2)) # 6
    print(thingy.maxDistinctElements([4, 4, 4, 4], 1)) # 3
    # print(thingy.maxDistinctElements()) # 
    # print(thingy.maxDistinctElements()) # 


if __name__ == "__main__":
    main()