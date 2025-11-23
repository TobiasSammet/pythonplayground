# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

# Example 1:
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.

# Example 2:
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.

# Constraints:
#     1 <= nums.length <= 105
#     0 <= k <= nums.length
#     nums[i] is 0 or 1

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        length: int = len(nums)
        try: 
            lastSpot: int = nums.index(1)
        except:
            return True
        for i in range(lastSpot+1, length):
            if nums[i] == 1:
                temp = i - lastSpot
                if temp <= k:
                    return False
                lastSpot = i

        return True
    


def main():
    thingy = Solution()
    print(thingy.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2)) # True
    print(thingy.kLengthApart([1, 0, 0, 1, 0, 1], 2)) # False
    print(thingy.kLengthApart([0, 0, 0, 0, 0, 0], 2)) # False
    # print(thingy.kLengthApart()) # 
    

if __name__ == "__main__":
    main()