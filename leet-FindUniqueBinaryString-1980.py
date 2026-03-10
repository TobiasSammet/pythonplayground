# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

# Example 1:
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

# Example 2:
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.

# Example 3:
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

# Constraints:
#     n == nums.length
#     1 <= n <= 16
#     nums[i].length == n
#     nums[i] is either '0' or '1'.
#     All the strings of nums are unique.

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if len(nums) == 0:
            return ""
        numbers: List[int] = []
        length: int = len(nums[0])

        for val in nums:
            numbers.append(int(val, 2))
            
        numbers.sort()

        i: int = 0
        while(i < len(nums)):
            if (numbers[i] != i):
                retVal: str = bin(i)[2:].rjust(length, "0")
                return retVal
            i += 1
        
        return bin(i)[2:].rjust(length, "0")

        return "00"
    

def main():
    thingy = Solution()
    # assert thingy.findDifferentBinaryString(['01', '10']) == "00", "Test Case Failed"
    assert thingy.findDifferentBinaryString(['00', '01']) == "10", "Test Case Failed"
    assert thingy.findDifferentBinaryString(['111', '011', '001']) == "000", "Test Case Failed"
    # assert thingy.findDifferentBinaryString == "", "Test Case Failed"


if __name__ == "__main__":
    main()          
    