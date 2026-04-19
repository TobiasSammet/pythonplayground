# You are given an integer array nums.
# A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
# The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
# Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

# Example 1:
# Input: nums = [1,2,1,1,3]
# Output: 6
# Explanation:
# The minimum distance is achieved by the good tuple (0, 2, 3).
# (0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

# Example 2:
# Input: nums = [1,1,2,3,2,1,2]
# Output: 8
# Explanation:
# The minimum distance is achieved by the good tuple (2, 4, 6).
# (2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

# Example 3:
# Input: nums = [1]
# Output: -1
# Explanation:
# There are no good tuples. Therefore, the answer is -1.

# Constraints:
#     1 <= n == nums.length <= 100
#     1 <= nums[i] <= n


from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        length = len(nums)
        if (length <= 2):
             return -1
        ret_val = float('inf')
        sorted = nums.copy()
        sorted.sort()

        numbersOfInterest: List[int] = []
  
        i: int = 0
        while i < length-2:
            tempVal = sorted[i]
            if (sorted[i] == sorted[i + 2]):
                numbersOfInterest.append(sorted[i])
                while i < length - 1 and sorted[i + 1] == tempVal:
                    i+=1
            else:
                i+=1
    
        for i in range(len(numbersOfInterest)):
            pos1 = float('inf')
            pos2 = float('inf')
            pos3 = float('inf')
            tempVal = numbersOfInterest[i]
            for j in range(length):
                if nums[j] == tempVal:
                    pos1 = pos2
                    pos2 = pos3
                    pos3 = j
                    if pos1 != float('inf'):
                        distance = abs(pos1 - pos2) + abs(pos2 - pos3) + abs(pos3 - pos1)
                        ret_val = min(ret_val, distance)
        
        if (ret_val == float('inf')):
            return -1
        return int(ret_val)


def main():
    thingy = Solution()
    assert thingy.minimumDistance([1,2,1,1,3]) == 6, "Test Case Failed"
    assert thingy.minimumDistance([1,1,2,3,2,1,2]) == 8, "Test Case Failed"
    assert thingy.minimumDistance([1]) == -1, "Test Case Failed"
    # assert thingy.minimumDistance() == 0, "Test Case Failed"

if __name__ == "__main__":
    main()    