# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Constraints:
#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     0 <= k <= 105

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        the_set = set()
        for num in nums:
            if num in the_set:
                return True
            the_set.add(num)        

        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        the_set = set()
        i: int = 0
        for num in nums:
            if i - k > 0:
                the_set.remove(nums[i-k-1])
            if num in the_set:
                return True
            the_set.add(num)        
            i += 1

        return False

    
def main():
    thing = Solution()
    # assert thing.containsDuplicate([1,2,3,1]) == True, "Test Case Failed"
    # assert thing.containsDuplicate([1,2,3,4]) == False, "Test Case Failed"
    # assert thing.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True, "Test Case Failed"
    # assert thing.containsDuplicate() == False, "Test Case Failed"

    assert thing.containsNearbyDuplicate(nums = [1,2,3,1], k = 3) == True, "Test Case Failed"
    assert thing.containsNearbyDuplicate([1,0,1,1], k = 1) == True, "Test Case Failed"
    assert thing.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2) == False, "Test Case Failed"
    # assert thing.containsNearbyDuplicate() == False, "Test Case Failed"


if __name__ == "__main__":
    main()