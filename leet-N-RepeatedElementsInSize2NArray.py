# You are given an integer array nums with the following properties:
#     nums.length == 2 * n.
#     nums contains n + 1 unique elements.
#     Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

# Example 1:
# Input: nums = [1,2,3,3]
# Output: 3

# Example 2:
# Input: nums = [2,1,2,5,3,2]
# Output: 2

# Example 3:
# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5

# Constraints:
#     2 <= n <= 5000
#     nums.length == 2 * n
#     0 <= nums[i] <= 104
#     nums contains n + 1 unique elements and one of them is repeated exactly n times.

from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mySet = set()

        for i in range(0, len(nums)):
            num = nums[i]
            if num in mySet:
                return num
            mySet.add(num)
        return -1

    # def repeatedNTimes(self, nums: List[int]) -> int:
    #     length: int = len(nums)
    #     nums.sort()
        
    #     for i in range(1, length):
    #         if (nums[i-1] == nums[i]):
    #             return nums[i]
    #     return -1


def main():
    thing = Solution()
    print(thing.repeatedNTimes([1,2,3,3])) # 3
    print(thing.repeatedNTimes([2,1,2,5,3,2])) # 2
    print(thing.repeatedNTimes([5,1,5,2,5,3,5])) # 5

    assert thing.repeatedNTimes([1,2,3,3]) == 3, "Test Case Failed"


if __name__ == "__main__":
    main()        