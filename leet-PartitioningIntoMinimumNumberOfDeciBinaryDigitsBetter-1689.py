# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
# Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

# Example 1:
# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32

# Example 2:
# Input: n = "82734"
# Output: 8

# Example 3:
# Input: n = "27346209830709182346"
# Output: 9

# Constraints:
#     1 <= n.length <= 10^5


class Solution:
    def minPartitions(self, n: str) -> int:
        length = len(n)
        if length == 0:
            return 0
        retVal: int = 0
        for char in n:
            retVal = max(retVal, int(char))
            if retVal == 9:
                return 9

        return retVal
    

def main():
    thingy = Solution()
    assert thingy.minPartitions("32") == 3, "Test Case Failed"
    assert thingy.minPartitions("82734") == 8, "Test Case Failed"
    assert thingy.minPartitions("27346209830709182346") == 9, "Test Case Failed"
    # assert thingy.minPartitions() == 1, "Test Case Failed"
    

if __name__ == "__main__":
    main()