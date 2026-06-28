# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.

# Example 2:
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

# Constraints:
#     1 <= nums1.length, nums2.length <= 10^5
#     1 <= nums1[i], nums2[j] <= 10^9
#     Both nums1 and nums2 are sorted in non-decreasing order.


from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i: int = 0
        j: int = 0
        length1: int = len(nums1)
        length2: int = len(nums2)
        if length1 == 0 or length2 == 0:
            return -1
        while True:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
                if i >= length1:
                    return  -1
            else:
                j += 1
                if j >= length2:
                    return  -1



def main():
    thingy = Solution()
    assert thingy.getCommon(nums1 = [1,2,3], nums2 = [2,4]) == 2, "Test Case Failed"
    assert thingy.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5]) == 2, "Test Case Failed"
    assert thingy.getCommon([2, 4, 6], [1, 3, 5]) == -1, "Test Case Failed"
    assert thingy.getCommon([1, 2, 3, 4, 5], [100, 101, 102, 103]) == -1, "Test Case Failed"
    # assert thingy.getCommon() == , "Test Case Failed"

if __name__ == "__main__":
    main()